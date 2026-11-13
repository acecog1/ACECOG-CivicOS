import fs from 'node:fs';
import crypto from 'node:crypto';
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const [file,expected]=process.argv.slice(2),raw=fs.readFileSync(file);
if(!/^[0-9a-f]{64}$/.test(expected)||sha(raw)!==expected)throw Error('Archive checksum mismatch');
const entries=new Map();let p=0;
while(raw.readUInt32LE(p)===0x04034b50){const method=raw.readUInt16LE(p+8),len=raw.readUInt32LE(p+18),nl=raw.readUInt16LE(p+26),el=raw.readUInt16LE(p+28),name=raw.subarray(p+30,p+30+nl).toString(),start=p+30+nl+el;if(method!==0||entries.has(name)||name.startsWith('/')||name.includes('\\')||name.includes(':')||name.split('/').includes('..'))throw Error('Unsafe or unsupported entry');entries.set(name,raw.subarray(start,start+len));p=start+len;}
const m=JSON.parse(entries.get('integrity.json'));
if(m.releasable!==false||m.license_sbom_approved!==false||entries.size!==m.files.length+1)throw Error('Gate/file set mismatch');
const seen=new Set();for(const f of m.files){if(seen.has(f.path)||!entries.has(f.path)||entries.get(f.path).length!==f.bytes||sha(entries.get(f.path))!==f.sha256)throw Error('Payload mismatch '+f.path);seen.add(f.path);}
console.log('PASS: archive checksum, exact file set, '+m.files.length+' payload digests and HOLD flags');
