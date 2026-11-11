// Real Chromium regressions for BG-1. Build with scripts/build_site.py first.
const { test, before, after } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const http = require('node:http');
const { chromium } = require('playwright');
const root = path.resolve(__dirname, '../../build/site');
const evidence = path.resolve(__dirname, '../../build/site-evidence');
const record = JSON.parse(fs.readFileSync(path.join(root, 'events.json')));
let server, browser, base;
before(async () => {
  fs.mkdirSync(evidence, { recursive: true });
  server = http.createServer((req, res) => {
    const file = path.join(root, new URL(req.url, 'http://localhost').pathname);
    if (!file.startsWith(root + path.sep) || !fs.existsSync(file) || !fs.statSync(file).isFile()) {
      res.writeHead(404).end(); return;
    }
    const types = {'.html':'text/html', '.js':'text/javascript', '.css':'text/css', '.json':'application/json'};
    res.setHeader('Content-Type', types[path.extname(file)] || 'application/octet-stream');
    fs.createReadStream(file).pipe(res);
  });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  base = `http://127.0.0.1:${server.address().port}`;
  browser = await chromium.launch({headless: true,
    ...(process.env.CHROMIUM_PATH ? {executablePath: process.env.CHROMIUM_PATH} : {})});
});
after(async () => { await browser?.close(); await new Promise(resolve => server.close(resolve)); });

async function checkRecord(transform, success = false) {
  const page = await browser.newPage({reducedMotion:'reduce'});
  try {
    await page.route('**/events.json', route => route.fulfill({json:transform(structuredClone(record))}));
    await page.goto(base + '/verify.html');
    await page.waitForFunction(() => {
      const text = document.querySelector('.chain-status').textContent;
      return /check out|failed|doesn't match|couldn't be loaded/.test(text);
    });
    const text = await page.locator('.chain-status').textContent();
    assert.equal(text.includes(`All ${record.events.length} records check out`), success, text);
    if (!success) assert.equal(await page.locator('[data-tamper]').isVisible(), false);
  } finally { await page.close(); }
}
test('complete published record verifies', () => checkRecord(r => r, true));
const invalid = {
  'empty chain': r => ({...r, events:[]}),
  'truncated suffix with original head': r => ({...r, events:r.events.slice(0,-1)}),
  'self-consistent prefix still disagrees with page': r => ({...r, event_count:r.events.length-1,
    chain_head:r.events.at(-2).hash, events:r.events.slice(0,-1)}),
  'wrong declared head': r => ({...r, chain_head:'f'.repeat(64)}),
  'wrong declared count': r => ({...r, event_count:1}),
  'missing count': r => { delete r.event_count; return r; },
  'reordered events': r => { [r.events[1],r.events[2]] = [r.events[2],r.events[1]]; return r; },
  'mutated event text': r => { r.events[2].text += ' '; return r; },
  'wrong terminal hash': r => { r.events.at(-1).hash='f'.repeat(64); return r; },
  'wrong sequence': r => { r.events[2].seq=999; return r; },
  'malformed event': r => { r.events[2]=null; return r; },
  'missing events': r => { delete r.events; return r; },
};
for (const [name, transform] of Object.entries(invalid)) test(`reject ${name}`, () => checkRecord(transform));
for (const failure of ['http', 'json']) test(`unavailable record is never successful: ${failure}`, async () => {
  const page = await browser.newPage({reducedMotion:'reduce'});
  try {
    await page.route('**/events.json', route => route.fulfill(failure === 'http' ?
      {status:503,body:'unavailable'} : {contentType:'application/json',body:'{'}));
    await page.goto(base+'/verify.html');
    await page.waitForFunction(() => document.querySelector('.chain-status').textContent.includes("couldn't be loaded"));
    assert.equal(await page.locator('[data-tamper]').isVisible(), false);
  } finally { await page.close(); }
});
test('tamper demonstration fails, then reload verifies intact record', async () => {
  const page = await browser.newPage({reducedMotion:'reduce'});
  try {
    await page.goto(base + '/verify.html');
    await page.waitForFunction(() => document.querySelector('.chain-status').textContent.includes('check out'));
    await page.locator('[data-tamper]').click();
    await page.waitForFunction(() => document.querySelector('.chain-status').textContent.includes("doesn't match"));
    await page.locator('[data-tamper]').click();
    await page.waitForFunction(() => document.querySelector('.chain-status').textContent.includes('check out'));
  } finally { await page.close(); }
});
for (const width of [1280, 390]) test(`pages accessible with no external requests at ${width}px`, async () => {
  const page = await browser.newPage({viewport:{width,height:900}, reducedMotion:'reduce'});
  const errors=[], external=[];
  page.on('pageerror', e => errors.push(e.message));
  page.on('request', r => { if (!r.url().startsWith(base+'/')) external.push(r.url()); });
  try {
    for (const file of ['index.html','verify.html','built.html','about.html']) {
      await page.goto(base+'/'+file);
      if (file==='index.html' || file==='verify.html') await page.waitForFunction(() =>
        document.querySelector('.chain-status').textContent.includes('check out'));
      await page.addScriptTag({path:require.resolve('axe-core/axe.min.js')});
      const results = await page.evaluate(async () => {
        const scan=await axe.run(document, {runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa']}});
        return {violations:scan.violations,incomplete:scan.incomplete};
      });
      fs.writeFileSync(path.join(evidence, `${width}-${file}.axe.json`), JSON.stringify(results,null,2));
      assert.deepEqual(results.violations, [], `${width} ${file}: ${JSON.stringify(results.violations)}`);
      assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), file);
      for (const region of await page.locator('.scroll').all()) {
        // Reach each region through actual sequential keyboard navigation, not programmatic focus.
        let reached=false;
        for (let i=0;i<60;i++) {
          await page.keyboard.press('Tab');
          if (await region.evaluate(el => document.activeElement===el)) { reached=true; break; }
        }
        assert.ok(reached, 'scrolling table must be reachable by Tab');
        assert.equal(await region.evaluate(el => document.activeElement===el), true);
        assert.notEqual(await region.evaluate(el => getComputedStyle(el).outlineStyle), 'none');
        if (await region.evaluate(el => el.scrollWidth>el.clientWidth)) {
          await page.keyboard.press('ArrowRight');
          await page.waitForFunction(() => document.activeElement.scrollLeft>0);
          await page.keyboard.press('Home');
          await region.evaluate(el => { el.scrollLeft=0; });
        }
      }
      // Inspect accessible landmark/table names through the browser's accessibility representation.
      const aria = await page.locator('main').ariaSnapshot();
      fs.writeFileSync(path.join(evidence, `${width}-${file}.aria.txt`), aria);
      assert.match(aria, /heading/);
      await page.screenshot({path:path.join(evidence, `${width}-${file}.png`),fullPage:true});
    }
    assert.deepEqual(errors, []); assert.deepEqual(external, []);
  } finally { await page.close(); }
});
