import fs from 'node:fs';
import crypto from 'node:crypto';
import {spawnSync} from 'node:child_process';
import path from 'node:path';
const root=path.resolve(import.meta.dirname,'..'),zip=path.join(root,'docs/evidence/bg2-beta-packet-20261113/licensing-source-review.zip'),raw=fs.readFileSync(zip),hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const e=raw.length-22,cd=raw.readUInt32LE(e+16),second=cd+46+raw.readUInt16LE(cd+28);
const cases=[
 ['central-offset',b=>{b.writeUInt32LE(1,cd+42);return b;}],
 ['central-crc',b=>{b.writeUInt32LE(0,cd+16);return b;}],
 ['central-name',b=>{b[cd+46]^=1;return b;}],
 ['duplicate-name',b=>{const byLength=new Map();let p=cd;while(p<e){const n=b.readUInt16LE(p+28);if(byLength.has(n)){const prev=byLength.get(n),o=b.readUInt32LE(p+42);b.copy(b,p+46,prev+46,prev+46+n);b.copy(b,o+30,prev+46,prev+46+n);return b;}byLength.set(n,p);p+=46+n;}throw Error('No equal-length names');}],
 ['trailing-entry',b=>Buffer.concat([b,b.subarray(0,31)])],
 ['missing-entry-count',b=>{b.writeUInt16LE(b.readUInt16LE(e+10)-1,e+10);return b;}],
 ['corrupt-payload',b=>{b[100]^=1;return b;}],
 ['truncated',b=>b.subarray(0,b.length-1)]
];
const tmp=path.join(root,'build/packet-negative.zip');
for(const [name,mutate] of cases){const b=mutate(Buffer.from(raw));fs.writeFileSync(tmp,b);const r=spawnSync(process.execPath,[path.join(root,'scripts/verify_bg2_beta_packet.mjs'),tmp,hash(b)],{encoding:'utf8'});if(r.status===0)throw Error('Accepted '+name);console.log('REJECT '+name+' with recomputed archive digest');}
fs.unlinkSync(tmp);
