// Evidence recovery only. Does not rebuild or approve the shipped runtime.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {spawnSync} from 'node:child_process';
import zlib from 'node:zlib';
const root=path.resolve(import.meta.dirname,'..'), out=path.join(root,'docs/evidence/bg2-mandatory-groups-20261113');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const put=(n,b)=>{const p=path.join(out,n);fs.mkdirSync(path.dirname(p),{recursive:true});fs.writeFileSync(p,b);};
const json=(n,v)=>put(n,JSON.stringify(v,null,2)+'\n');
const previous=fs.existsSync(path.join(out,'recovered-files.json'))?JSON.parse(fs.readFileSync(path.join(out,'recovered-files.json'))):[];
const records=[],sources=[];
function archive(key,file,url,select,expected){
 const raw=fs.readFileSync(file),h=sha(raw);if(expected&&h!==expected)throw Error('Archive digest '+key);
 const listing=spawnSync('tar',['-tf',file],{maxBuffer:20e6,encoding:'utf8'});if(listing.status)throw Error(listing.stderr);
 sources.push({key,url,bytes:raw.length,sha256:h,archive_basename:path.basename(file),retrieval:'Download URL, verify SHA-256, then extract listed exact member paths. Source archive hash alone does not attest prebuilt binary correspondence.'});
 for(const member of listing.stdout.split(/\r?\n/).filter(n=>n&&!n.endsWith('/'))){
  const relative=member.split('/').slice(1).join('/');if(!select(relative))continue;
  const cached=previous.find(r=>r.archive_sha256===h&&r.archive_member===member&&r.extraction==='FULL_ORIGINAL_FILE');
  let b;if(cached){b=fs.readFileSync(path.join(out,cached.path));if(sha(b)!==cached.sha256)throw Error('Cached original mismatch');}else{const r=spawnSync('tar',['-xOf',file,member],{maxBuffer:40e6});if(r.status)throw Error(String(r.stderr));b=r.stdout;}
  let mode='FULL_ORIGINAL_FILE',original=sha(b),length=b.length;
  if(relative==='sqlite3.c'){let end=0;for(let line=0;line<160;line++){end=b.indexOf(10,end)+1;if(!end)throw Error('SQLite prefix');}b=b.subarray(0,end);if(!b.includes(Buffer.from('author disclaims copyright')))throw Error('Missing SQLite disclaimer');mode='EXACT_FIRST_160_LINES';}
  const dest='upstream/'+key+'/'+relative;put(dest,b);records.push({key,source_url:url,archive_sha256:h,archive_member:member,path:dest,sha256:sha(b),bytes:b.length,original_file_sha256:original,original_file_bytes:length,extraction:mode,applicability:'CANDIDATE_NOT_HUMAN_ACCEPTED'});
 }
}
const old=path.resolve(root,'../security-review/compiled-evidence/archives');
archive('rust-1.97.1',path.join(root,'build/rustc-1.97.1.tar.gz'),'https://static.rust-lang.org/dist/2026-07-16/rustc-1.97.1-x86_64-unknown-linux-gnu.tar.gz',n=>/^(LICENSE-APACHE|LICENSE-MIT|COPYRIGHT|version|git-commit-hash)$/.test(n)||n.startsWith('rustc/share/doc/rust/')&&(/COPYRIGHT.*html$/.test(n)||n.includes('/licenses/')),'1c441e430c1cca49dff54a8d59c41038bf6f79f7b8756596cb2f36511a015eba');
archive('rust-std-emscripten',path.join(root,'build/rust-std-1.97.1-wasm32-unknown-emscripten.tar.gz'),'https://static.rust-lang.org/dist/2026-07-16/rust-std-1.97.1-wasm32-unknown-emscripten.tar.gz',n=>/^(LICENSE-APACHE|LICENSE-MIT|COPYRIGHT|version|git-commit-hash)$/.test(n),'4878677947b25d42db0962473a5ab6a96c2533cc279feebce1cca6ab8f47af7f');
archive('recipes',path.join(root,'build/recipes.tar.gz'),'https://codeload.github.com/pyodide/pyodide-recipes/tar.gz/fc8587207ecbf0fb54305d5da25ab7ed70f126d3',n=>/^packages\/(libf2c|libopenblas|scipy|numpy|rpds-py|libboost|libhiwire|sqlite3)\//.test(n));
archive('pyodide',path.join(old,'pyodide-source.tar.gz'),'https://codeload.github.com/pyodide/pyodide/tar.gz/b1e4fcc2488962f6360a97f19b9982d6fdb5d16f',n=>/^(Makefile.envs|LICENSE|cpython\/Makefile|cpython\/Setup.local|emsdk\/Makefile)$/.test(n)||/^(cpython|emsdk)\/patches\//.test(n));
archive('cpython',path.join(old,'cpython.tar.gz'),'https://www.python.org/ftp/python/3.14.2/Python-3.14.2.tgz',n=>/^(LICENSE|Doc\/license.rst|Modules\/expat\/COPYING)$/.test(n)||/^Modules\/(_hacl|_decimal\/libmpdec)\//.test(n)&&/\.(h|c|txt)$/.test(n));
archive('emscripten',path.join(old,'emscripten.tar.gz'),'https://codeload.github.com/emscripten-core/emscripten/tar.gz/5.0.3',n=>/^(LICENSE|src\/lib\/liblz4.js|third_party\/mini-lz4.js|system\/lib\/libc\/musl\/COPYRIGHT)$/.test(n)||/^system\/lib\/(libcxx|libcxxabi|libunwind|compiler-rt)\/.*LICENSE/.test(n));
archive('sqlite',path.join(old,'sqlite.tar.gz'),'https://www.sqlite.org/2022/sqlite-autoconf-3390000.tar.gz',n=>n==='sqlite3.c');
archive('hiwire',path.join(old,'hiwire.tar.gz'),'https://codeload.github.com/pyodide/hiwire/tar.gz/6a1e67280a15d929ebeceee54a6358c9c8d5f697',n=>/LICENSE|COPYRIGHT/.test(n));
for(const [key,file,url]of [
 ['scipy','scipy-sdist.tar.gz','https://files.pythonhosted.org/packages/source/s/scipy/scipy-1.18.0.tar.gz'],
 ['numpy','numpy.tar.gz','https://codeload.github.com/numpy/numpy/tar.gz/v2.4.6'],
 ['openblas','openblas.tar.gz','https://codeload.github.com/OpenMathLib/OpenBLAS/tar.gz/76f1be470c9b9f80dc6e27407e13b975df436489'],
 ['libf2c','clapack.tar.gz','https://web.archive.org/web/20260509221335/https://www.netlib.org/clapack/clapack.tgz'],
 ['rpds','rpds-sdist.tar.gz','https://files.pythonhosted.org/packages/source/r/rpds_py/rpds_py-0.30.0.tar.gz'],
 ['libffi','libffi.tar.gz','https://codeload.github.com/libffi/libffi/tar.gz/f08493d249d2067c8b3207ba46693dd858f95db3'],
 ['xz','xz.tar.gz','https://codeload.github.com/xz-mirror/xz/tar.gz/v5.2.2'],
 ['zstd','zstd.tar.gz','https://codeload.github.com/python/cpython-source-deps/tar.gz/refs/tags/zstd-1.5.7']
])archive(key,path.join(old,file),url,()=>false);
json('source-archives.json',sources);json('recovered-files.json',records);
// Verify the accepted archive bytes and each ledger-associated original against actual runtime.
function unzip(b){let e=b.length-22;while(e>=0&&b.readUInt32LE(e)!==0x06054b50)e--;if(e<0)throw Error('ZIP');const m=new Map();let p=b.readUInt32LE(e+16);for(let i=0;i<b.readUInt16LE(e+10);i++){const method=b.readUInt16LE(p+10),len=b.readUInt32LE(p+20),nl=b.readUInt16LE(p+28),el=b.readUInt16LE(p+30),cl=b.readUInt16LE(p+32),o=b.readUInt32LE(p+42),n=b.subarray(p+46,p+46+nl).toString(),s=o+30+b.readUInt16LE(o+26)+b.readUInt16LE(o+28);if(m.has(n)||![0,8].includes(method))throw Error('ZIP entry');const v=b.subarray(s,s+len);m.set(n,method===8?zlib.inflateRawSync(v):v);p+=46+nl+el+cl;}return m;}
const ledger=JSON.parse(fs.readFileSync(path.join(root,'docs/evidence/bg2-shipped-ledger-20261112/ledger.json'))),runtime=fs.readFileSync(path.join(root,'../CivicOS-release/build/exact-review.zip'));
if(sha(runtime)!==ledger.artifact.inner_zip_sha256)throw Error('Runtime baseline');const rt=unzip(runtime);
const release=JSON.parse(rt.get('release-manifest.json'));if(release.releasable!==false||release.license_sbom_approved!==false)throw Error('Runtime HOLD');
for(const [n,b]of rt)if(n!=='release-manifest.json'&&sha(b)!==release.file_sha256[n])throw Error('Runtime payload '+n);
if(rt.size!==208||Object.keys(release.file_sha256).length!==207)throw Error('Runtime inventory count');
for(const n of ledger.notices)if(sha(rt.get(n.artifact_path))!==n.sha256)throw Error('Notice '+n.path);
let embedded=0;for(const p of ledger.packages){const b=rt.get(p.artifact_path);if(sha(b)!==p.sha256)throw Error('Package');const w=unzip(b);for(const n of p.embedded_notice_entries){if(sha(w.get(n.member_path))!==n.sha256)throw Error('Wheel notice');embedded++;}}
for(const c of ledger.core)if(sha(rt.get(c.path||c.artifact_path))!==c.sha256)throw Error('Core '+JSON.stringify(c));
let native=0;for(const p of ledger.packages){const w=unzip(rt.get(p.artifact_path)),expected=ledger.members.filter(m=>m.wheel===path.posix.basename(p.artifact_path));if([...w.keys()].filter(n=>/\.(so|a)$/.test(n)).length!==expected.length)throw Error('Native member set');for(const m of expected){const b=w.get(m.member_path);if(!b||b.length!==m.bytes||sha(b)!==m.member_sha256)throw Error('Native '+m.member_path);native++;}}
if(native!==123)throw Error('Native count');
for(const x of ledger.excluded)if([...rt.values()].some(b=>sha(b)===x.sha256))throw Error('Excluded screenshot delivered');
json('component-source-matrix.json',ledger.components.map(c=>({component_id:c.id,name:c.name,source_notice_records:ledger.notices.filter(n=>c.notice_ids.includes(n.path)).map(n=>({source_url:n.source_location,source_path:n.source_path,notice_sha256:n.sha256,original_notice_id:n.path})),delivered_member_refs:ledger.members.filter(m=>m.associations.some(a=>a.component_id===c.id)).map(m=>({wheel:m.wheel,path:m.member_path,sha256:m.member_sha256})),source_archive_keys:sources.filter(s=>c.id===s.key||c.id.startsWith(s.key+'-')).map(s=>s.key),modification_status:'ACTUAL_SELECTED_BUILD_CORRESPONDENCE_UNCONFIRMED',human_legal_decision:'PENDING',scope:'Candidate associations; notice/source identity does not prove linked source selection'})));
const supplement=fs.readFileSync(path.join(root,'docs/evidence/bg2-beta-packet-20261113/licensing-source-review.zip'));if(sha(supplement)!=='a1192e12a77139a14134fab7323737cd4cee08768b433da884423714295e808d')throw Error('Supplement baseline');
const sp=unzip(supplement),integrity=JSON.parse(sp.get('integrity.json'));
json('verification.json',{role:'BUILDER_RECHECK_NOT_INDEPENDENT_QA_OR_LEGAL',runtime_sha256:sha(runtime),runtime_bytes:runtime.length,supplement_sha256:sha(supplement),supplement_bytes:supplement.length,supplement_entries:sp.size,notice_records_checked:ledger.notices.length,wheel_packages_checked:ledger.packages.length,embedded_notice_files_checked:embedded,core_files_checked:ledger.core.length,native_member_records:ledger.members.length,recovered_files:records.length,release:'HOLD',releasable:false,license_sbom_approved:false});
console.log(JSON.stringify({recovered:records.length,sources:sources.length,notice_records:ledger.notices.length,embedded}));
