import fs from 'node:fs';
import crypto from 'node:crypto';
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const [file,expected]=process.argv.slice(2),raw=fs.readFileSync(file);
const fail=s=>{throw Error(s);};
if(!/^[0-9a-f]{64}$/.test(expected)||sha(raw)!==expected)fail('Archive checksum mismatch');
function crc(b){let c=0xffffffff;for(const v of b){c^=v;for(let j=0;j<8;j++)c=(c>>>1)^((c&1)?0xedb88320:0);}return(c^0xffffffff)>>>0;}
// Strict reader for this generator's stored ZIP subset. Reject all other formats.
const e=raw.length-22;
if(e<0||raw.readUInt32LE(e)!==0x06054b50||raw.readUInt16LE(e+20)!==0||raw.readUInt32LE(e+4)!==0)fail('Invalid end/disk/comment/trailing data');
const count=raw.readUInt16LE(e+10),size=raw.readUInt32LE(e+12),offset=raw.readUInt32LE(e+16);
if(count!==raw.readUInt16LE(e+8)||offset+size!==e)fail('Directory bounds/count');
const entries=new Map();let p=offset,local=0;
for(let i=0;i<count;i++){
 if(p+46>e||raw.readUInt32LE(p)!==0x02014b50)fail('Directory signature');
 const flags=raw.readUInt16LE(p+8),method=raw.readUInt16LE(p+10),checksum=raw.readUInt32LE(p+16),len=raw.readUInt32LE(p+20),ulen=raw.readUInt32LE(p+24),nl=raw.readUInt16LE(p+28),el=raw.readUInt16LE(p+30),cl=raw.readUInt16LE(p+32),o=raw.readUInt32LE(p+42);
 if(flags!==0x800||method!==0||len!==ulen||el||cl||raw.readUInt16LE(p+34)||o!==local||p+46+nl>e)fail('Unsupported or inconsistent directory entry');
 const nb=raw.subarray(p+46,p+46+nl),name=nb.toString('utf8');
 if(!name||!Buffer.from(name).equals(nb)||entries.has(name)||name.startsWith('/')||name.includes('\\')||name.includes(':')||name.includes('\0')||name.split('/').some(x=>!x||x==='..'||x==='.'))fail('Unsafe/duplicate name');
 if(o+30>offset||raw.readUInt32LE(o)!==0x04034b50||raw.readUInt16LE(o+26)!==nl||raw.readUInt16LE(o+28)!==0)fail('Local header bounds');
 if(!raw.subarray(o+4,o+26).equals(raw.subarray(p+6,p+28))||!raw.subarray(o+30,o+30+nl).equals(nb))fail('Local/directory mismatch');
 const start=o+30+nl,end=start+len;
 if(end>offset)fail('Payload bounds');
 const b=raw.subarray(start,end);if(crc(b)!==checksum)fail('CRC mismatch');
 entries.set(name,b);local=end;p+=46+nl;
}
if(p!==e||local!==offset)fail('Unlisted/trailing ZIP entry');
const m=JSON.parse(entries.get('integrity.json'));
if(m.releasable!==false||m.license_sbom_approved!==false||entries.size!==m.files.length+1)fail('Gate/file set mismatch');
const seen=new Set(['integrity.json']);for(const f of m.files){if(seen.has(f.path)||!entries.has(f.path)||entries.get(f.path).length!==f.bytes||sha(entries.get(f.path))!==f.sha256)fail('Payload mismatch '+f.path);seen.add(f.path);}
const ledger=JSON.parse(entries.get('mapping/ledger.json')),notices=JSON.parse(entries.get('notice-index.json'));
const dispositions=JSON.parse(entries.get('dispositions.json'));
for(const d of dispositions){
 for(const id of d.required_original_notice_ids){const n=notices.find(n=>n.path===id);if(!n||sha(entries.get(n.packet_path))!==n.sha256)fail('Notice reference '+id);}
 for(const c of d.affected_core_assets)if(!ledger.core.some(x=>x.artifact_path===c.artifact_path&&x.sha256===c.sha256))fail('Core association');
 for(const p of d.affected_packages)if(!ledger.packages.some(x=>x.artifact_path===p.artifact_path&&x.sha256===p.sha256))fail('Package association');
 for(const uri of d.source_patch_evidence_uris)if(!entries.has(uri.notice_uri)||sha(entries.get(uri.notice_uri))!==uri.notice_sha256)fail('Source/notice reference');
 if(d.human_decision!=='PENDING_ACCEPT_OR_REJECT'||d.blocking!==true)fail('Unexpected decision state');
}
console.log('PASS: strict stored ZIP directory/local headers/CRC, exact file set, '+m.files.length+' payload digests, claim references and HOLD flags');
