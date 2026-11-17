import fs from 'node:fs/promises';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
function unzip(b){ var m=new Map(); var e=b.length-22; while(b.readUInt32LE(e)!==0x06054b50)e--; var p=b.readUInt32LE(e+16); for(var i=0;i<b.readUInt16LE(e+10);i++){var method=b.readUInt16LE(p+10),len=b.readUInt32LE(p+20),nl=b.readUInt16LE(p+28),el=b.readUInt16LE(p+30),cl=b.readUInt16LE(p+32),o=b.readUInt32LE(p+42),n=b.subarray(p+46,p+46+nl).toString();var s=o+30+b.readUInt16LE(o+26)+b.readUInt16LE(o+28);var d=b.subarray(s,s+len);if(m.has(n))throw Error('duplicate '+n);m.set(n,method===8?zlib.inflateRawSync(d):d);p+=46+nl+el+cl;}return m;}
const here = path.dirname(fileURLToPath(import.meta.url));
const fail = message => { throw new Error(message); };
export async function derive(zipPath) {
const raw = await fs.readFile(zipPath);
if (sha(raw) !== 'c8fa9aa4bf97ec977966167dde2eb02db3681f96b2486df614f2e74f64c85a52') fail('Wrong review ZIP');
const packet = unzip(raw);
const j = n => JSON.parse(packet.get(n) || fail('Missing '+n));
const release = j('release-manifest.json');
if (release.source_revision !== '8cd6031bd1dd7aff9e266c0abeb729d9d015bc59' || release.releasable !== false || release.license_sbom_approved !== false) fail('Wrong source/gates');
if (packet.size !== 208 || Object.keys(release.file_sha256).length !== 207) fail('Wrong package count');
for (const [n,b] of packet) { if(n.startsWith('/') || n.includes('\\') || n.split('/').includes('..')) fail('Unsafe name'); if(n !== 'release-manifest.json' && sha(b) !== release.file_sha256[n]) fail('Payload mismatch '+n); }
const prefix='third_party/compiled_notice_evidence/';
const manifest=j(prefix+'manifest.json'), inv=j('third_party/bg2-locked-native-inventory.json'), oldmap=j(prefix+'native-component-map.json');
if(manifest.acceptance !== 'HOLD' || inv.license_acceptance !== 'HOLD') fail('Wrong licensing gates');
const components=JSON.parse(await fs.readFile(path.join(here,'component-rules.json'),'utf8'));
const byId=new Map(components.map(c=>[c.id,c]));
const notices=manifest.records.map(r=>{const p=prefix+r.path;if(sha(packet.get(p)||fail('Missing notice '+p))!==r.sha256)fail('Notice mismatch '+p);return {...r,artifact_path:p,component_ids:components.filter(c=>c.notice_ids.includes(r.path)).map(c=>c.id),role:r.path.startsWith('originals/')?'PRESERVED_CONTEXT_APPLICABILITY_UNACCEPTED':'REVIEW_DOCUMENT_NOT_LICENSE_TEXT',disposition:components.some(c=>c.notice_ids.includes(r.path))?'ASSOCIATED_CANDIDATE_TEXT_NOT_ACCEPTED':r.path.includes('LAPACKE')||r.path.includes('/ctest/')||r.path.includes('/relapack/')?'OPTIONAL_OR_EXCLUDED_BUILD_CONTEXT_NOT_CONFIRMED_SHIPPED':r.path.includes('x86-')||r.path.includes('/svml/')||r.path.includes('/highway/')?'ARCHITECTURE_SELECTION_UNRESOLVED_NOT_CONFIRMED_WASM':r.path.startsWith('originals/')?'UNASSIGNED_SOURCE_BUILD_OR_PYTHON_CONTEXT_REQUIRES_APPLICABILITY_REVIEW':'SUPPORTING_REVIEW_DOCUMENT'};});
const noticeIds=new Set(notices.map(n=>n.path));
for(const c of components)for(const n of c.notice_ids)if(!noticeIds.has(n))fail('Unknown notice '+n);
const members=[];const packages=[];
for(const w of inv.wheels){
 const archivePath='vendor/pyodide/'+w.wheel, bytes=packet.get(archivePath)||fail('Missing wheel');
 // Exact artifact hash already verified; compare its inventory binding, not upstream network hashes.
 if(sha(bytes)!==w.wheel_sha256)fail('Wheel inventory binding');
 const entries=unzip(bytes), native=[...entries.keys()].filter(n=>/\.(so|wasm|a|dylib|dll|pyd)$|\.so(?:\.[0-9]+)+$/.test(n)).sort();
 if(JSON.stringify(native)!==JSON.stringify(w.native_members.map(m=>m.member_path).sort()))fail('Extra/missing native member');
 packages.push({package:w.package,version:w.version,artifact_path:archivePath,sha256:w.wheel_sha256,native_members:native.length,embedded_notice_entries:[...entries].filter(([n])=>/(?:^|\/)(?:LICENSE[^/]*|COPYING[^/]*|NOTICE[^/]*)$/i.test(n)).map(([n,b])=>({member_path:n,sha256:sha(b),presence:'DIRECT_WHEEL_TEXT',applicability:'NOT_ACCEPTED'})),presence:'DIRECT_ARCHIVE_MEMBER',python_source_attribution:'NOT_CLEARED_BY_NATIVE_LEDGER'});
 for(const m of w.native_members){
  const b=entries.get(m.member_path);if(!b||sha(b)!==m.sha256||b.length!==m.bytes)fail('Native mismatch');
  const prior=oldmap.members.find(x=>x.wheel===w.wheel&&x.member_path===m.member_path);if(!prior||prior.member_sha256!==m.sha256)fail('Inherited map mismatch');
  const p=m.member_path;const ids=[w.package==='numpy'?'numpy':w.package==='rpds-py'?'rpds':'scipy'];
  const add=(test,...values)=>{if(test)ids.push(...values);};
  add(p==='scipy.libs/libopenblas.so','openblas','lapack','libf2c');
  add(p.includes('/_uarray/'),'uarray');add(p.includes('/_duccfft/'),'duccfft');add(p.includes('/_dop.'),'dop');
  add(p.includes('/_fast_matrix_market/'),'fmm');add(p.includes('/_direct.'),'direct');add(p.includes('/_highspy/'),'highs');
  add(p.includes('/_lbfgsb.'),'lbfgsb');add(p.includes('/csgraph/_matching.'),'lapjvsp');add(p.includes('/_moduleTNC.'),'tnc');add(p.includes('/_trlib/'),'trlib');add(p.includes('/_superlu.'),'superlu');
  add(p.includes('/arpack/'),'arpack');add(p.includes('/_propack.'),'propack');add(p.includes('/_qhull.'),'qhull');
  add(p.startsWith('scipy/special/'),'xsf','boost');add(p.startsWith('scipy/'),'pybind11');
  add(p.includes('/_unuran/'),'unuran');add(p.includes('/_biasedurn.'),'biasedurn');add(p.startsWith('scipy/ndimage/'),'ndimage');
  add(p.startsWith('numpy/fft/'),'numpy-pocketfft');add(p.startsWith('numpy/linalg/'),'numpy-lapack');
  add(p.startsWith('numpy/_core/'),'numpy-core');add(p.startsWith('numpy/random/'),'numpy-random');
  add(w.package==='rpds-py','rust','crate-rpds-1.2.0','crate-pyo3-0.27.2','crate-pyo3-ffi-0.27.2','crate-triomphe-0.1.15','cargo-context');
  const associations=ids.map(id=>({component_id:id,grade:id===ids[0]?'DISTRIBUTED_PACKAGE_OWNER':id==='cargo-context'?'BUILD_LOCK_CONTEXT_NOT_PROVEN_RUNTIME':'SOURCE_GRAPH_OR_BINARY_MARKER_CANDIDATE_NOT_OBJECT_PROOF',notice_ids:byId.get(id).notice_ids}));
  members.push({wheel:w.wheel,wheel_sha256:w.wheel_sha256,member_path:p,bytes:m.bytes,member_sha256:m.sha256,presence:'DIRECT_EXACT_REVIEW_WHEEL_MEMBER',status:'UNKNOWN_BLOCKING',associations,inherited_component_candidates:prior.component_candidates,unresolved:['Selected source/header/object closure remains incomplete; module association is not exact linked-object proof','Qualified notice/source/license decision pending'],numerical_source_scope:w.package==='scipy'?p.split('/').slice(0,-1).join('/')+' at SciPy 1.18.0 source snapshot':'Package source snapshot; exact selection pending'});
 }
}
if(members.length!==123||new Set(members.map(m=>m.wheel+'!'+m.member_path)).size!==123||oldmap.members.length!==123)fail('Member coverage');
const coreIds=['pyodide','cpython','hiwire','libffi','liblzma','sqlite','zstd','zlib','bzip2','emscripten'];
const core=['pyodide.asm.wasm','pyodide.asm.mjs','pyodide.mjs','python_stdlib.zip'].map(n=>({artifact_path:'vendor/pyodide/'+n,sha256:sha(packet.get('vendor/pyodide/'+n)),presence:'DIRECT_ARCHIVE_MEMBER',component_candidates:coreIds,status:'UNKNOWN_BLOCKING',caveat:'Core-level candidate pool from preserved matrix; not proof every listed library occurs in each file. JS/stdlib source attribution remains incomplete.'}));
const ledger={schema:'ACECOG-BG2-SHIPPED-COMPONENT-LEDGER-v1',acceptance:'HOLD',releasable:false,human_legal_review:'NOT_RETAINED_NOT_ACCEPTED',scope:'123 native wheel members plus package/core presence. Not a whole-distribution clearance or object-level linkage bill.',artifact:{id:14011669639,run:43371657753,source_sha:release.source_revision,source_tree:release.source_tree_sha,inner_zip_sha256:sha(raw),inner_zip_bytes:raw.length,zip_entries:packet.size,payload_files:207,sbom_sha256:sha(packet.get('third_party/bg2-sbom.cdx.json')),inventory_sha256:sha(packet.get('third_party/bg2-locked-native-inventory.json')),compiled_manifest_sha256:sha(packet.get(prefix+'manifest.json')),prior_map_sha256:sha(packet.get(prefix+'native-component-map.json'))},packages,core,components,members,notices,excluded:manifest.excluded,open_build_receipts:manifest.open_build_receipts,global_unresolved:['Actual selected-source/build receipts and missing source-header notice texts','Pure Python/source components and generated runtime attribution not closed by native inventory','Qualified reviewer applicability/source sufficiency, license alternatives, exceptions, public-domain, MPL/AGPL and Qhull decisions','Independent exact-artifact QA; protected controls, native AT/device and real host/rollback; Owner final acceptance and separate publication GO']};
await fs.writeFile(path.join(here,'ledger.json'),JSON.stringify(ledger,null,2)+'\n');
const csv=v=>'"'+String(v).replaceAll('"','""')+'"';
const rows=[['wheel','wheel_sha256','member_path','member_sha256','bytes','component_ids','notice_paths','status'],...members.map(m=>[m.wheel,m.wheel_sha256,m.member_path,m.member_sha256,m.bytes,m.associations.map(a=>a.component_id).join(';'),[...new Set(m.associations.flatMap(a=>a.notice_ids))].join(';'),m.status])];
await fs.writeFile(path.join(here,'members.csv'),rows.map(r=>r.map(csv).join(',')).join('\n')+'\n');
const report={artifact:ledger.artifact,checks:{payload_digests:207,native_members:123,notice_records:notices.length,original_texts:notices.filter(n=>n.path.startsWith('originals/')).length,all_member_status:'UNKNOWN_BLOCKING',extra_missing_native_members:0,legal_approval:false},component_count:components.length};
await fs.writeFile(path.join(here,'verification.json'),JSON.stringify(report,null,2)+'\n');
return report;
}
if (typeof process !== 'undefined' && process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) console.log(JSON.stringify(await derive(process.argv[2])));
