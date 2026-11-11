// Real Chromium checks of the localhost-only Riverbend development laboratory.
// Runs actual CivicOS Python engine, not a mocked comparison endpoint.
const { test, before, after } = require("node:test");
const assert = require("node:assert/strict");
const { spawn } = require("node:child_process");
const net = require("node:net");
const path = require("node:path");
const { chromium } = require("playwright");

let browser, processHandle, base;
let output = "";

async function freePort() {
  const s = net.createServer();
  await new Promise(resolve => s.listen(0, "127.0.0.1", resolve));
  const p = s.address().port;
  await new Promise(resolve => s.close(resolve));
  return p;
}

async function running(url) {
  for (let i=0; i<55; i++) {
    try {
      const r = await fetch(url + "/api/config");
      if (r.ok) return;
    } catch (e) {
      // Process may not be listening yet.
    }
    await new Promise(resolve => setTimeout(resolve, 150));
  }
  throw new Error("Local lab server failed to start: " + output.slice(0, 1200));
}

before(async () => {
  const port = await freePort();
  const script = path.resolve(__dirname, "../lab_preview_server.py");
  base = "http://127.0.0.1:" + port;
  processHandle = spawn("python", ["-u", script, "--port", String(port)], {
    cwd: path.resolve(__dirname, "../.."),
    stdio:["ignore", "pipe", "pipe"],
  });
  processHandle.stdout.on("data", chunk => output += chunk.toString());
  processHandle.stderr.on("data", chunk => output += chunk.toString());
  await running(base);
  browser = await chromium.launch({headless:true});
});

after(async () => {
  await browser?.close();
  if (processHandle && !processHandle.killed) processHandle.kill();
});

async function openLab(width=390) {
  const context = await browser.newContext({viewport:{width,height:900}, reducedMotion:"reduce", bypassCSP:true});
  const page = await context.newPage();
  const thirdParty = [], errors=[];
  page.on("request", req => {
    if (!req.url().startsWith(base + "/")) thirdParty.push(req.url());
  });
  page.on("pageerror", e => errors.push(e.message));
  await page.goto(base + "/");
  await page.waitForFunction(() => document.getElementById("form-status").textContent.includes("Ready"));
  return {context, page, thirdParty, errors};
}

test("visitor changes two votes; actual CivicOS rejects Plan A without ghost funding", async () => {
  const a = await openLab();
  try {
    await a.page.locator('input[name="vote-cara"][value="no"]').check();
    await a.page.locator('input[name="vote-dev"][value="no"]').check();
    await a.page.locator("#run").click();
    await a.page.waitForFunction(() => document.getElementById("form-status").textContent.includes("Run complete"), null, {timeout:30000});
    const content = await a.page.locator("#results").innerText();
    assert.match(content, /Reference/);
    assert.match(content, /Plan A approved/);
    assert.match(content, /Your alternative/);
    assert.match(content, /Plan A rejected/);
    assert.match(content, /No Plan A optimization, baseline or synthetic funding commitment/);
    assert.match(content, /2 yes . 3 no/);
    assert.deepEqual(a.thirdParty, []);
    assert.deepEqual(a.errors, []);
  } finally { await a.context.close(); }
});

test("budget and resource changes show engine-backed allocations and evidence", async () => {
  const a=await openLab(1280);
  try {
    await a.page.locator("#budget").fill("600000");
    await a.page.locator("#water").fill("12");
    await a.page.locator("#crew").fill("20");
    await a.page.locator("#run").click();
    await a.page.waitForFunction(() => document.getElementById("form-status").textContent.includes("Run complete"), null, {timeout:30000});
    const content=await a.page.locator("#results").innerText();
    assert.match(content, /Initiative funding comparison/);
    assert.match(content, /binding constraints/i);
    assert.match(content, /initiative allocations differ/);
    await a.page.locator("#results details summary").click();
    assert.match(await a.page.locator("#results details").innerText(), /alternative_chain_head/);
    assert.deepEqual(a.thirdParty, []);
    assert.deepEqual(a.errors, []);
  } finally { await a.context.close(); }
});

test("explicit seeded randomization, no automatic refresh randomization, mobile and a11y", async () => {
  const a=await openLab(320);
  try {
    assert.equal(await a.page.locator("#budget").inputValue(), "900000");
    await a.page.locator("#random").click();
    await a.page.waitForFunction(() => document.getElementById("seed-info").textContent.includes("Random input seed"));
    await a.page.reload();
    await a.page.waitForFunction(() => document.getElementById("form-status").textContent.includes("Ready"));
    assert.equal(await a.page.locator("#budget").inputValue(), "900000");
    assert.equal(await a.page.locator("#seed-info").innerText(), "");
    assert.equal(await a.page.locator(".vote-row").count(), 6);
    assert.match(await a.page.locator(".recused").innerText(), /Recused/);
    assert.equal(await a.page.locator('input[name="vote-eli"]').count(), 0);
    const m=await a.page.evaluate(() => ({
      viewport:document.documentElement.clientWidth,
      scroll:document.documentElement.scrollWidth
    }));
    assert.ok(m.scroll<=m.viewport+1,"Unexpected root overflow: "+JSON.stringify(m));
    await a.page.addScriptTag({path:require.resolve("axe-core/axe.min.js")});
    const ax=await a.page.evaluate(() => axe.run(document, {
      runOnly:{type:"tag",values:["wcag2a","wcag2aa","wcag21a","wcag21aa","wcag22aa"]}
    }));
    assert.deepEqual(ax.violations.map(v => ({id:v.id,nodes:v.nodes.map(n=>n.target)})), []);
    assert.deepEqual(a.thirdParty, []);
    assert.deepEqual(a.errors, []);
  } finally { await a.context.close(); }
});


test("P2 guided vote dilemma shows a governed refusal and no phantom allocation", async () => {
  const a=await openLab(1280);
  try {
    assert.match(await a.page.locator("#challenge-title").innerText(), /Choose a question/);
    await a.page.locator('[data-preset="votes"]').click();
    assert.equal(await a.page.locator('[data-preset="votes"]').getAttribute("aria-pressed"),"true");
    assert.equal(await a.page.locator('input[name="vote-cara"]:checked').inputValue(),"no");
    assert.equal(await a.page.locator('input[name="vote-dev"]:checked').inputValue(),"no");
    await a.page.locator("#run").click();
    await a.page.waitForFunction(() => document.getElementById("form-status").textContent.includes("Run complete"),null,{timeout:30000});
    assert.match(await a.page.locator("#results").innerText(), /Plan A rejected/);
    assert.match(await a.page.locator("#results").innerText(), /Not authorized/);
    assert.equal(await a.page.locator("#scenario-tools").isVisible(),true);
    assert.equal(await a.page.locator("#run-history li").count(),1);
    assert.deepEqual(a.thirdParty,[]);
    assert.deepEqual(a.errors,[]);
  } finally { await a.context.close(); }
});

test("P2 visual allocations and tab-only history reproduce user choices", async () => {
  const a=await openLab(1280);
  try {
    await a.page.locator('[data-preset="water"]').click();
    await a.page.locator("#run").click();
    await a.page.waitForFunction(() => document.getElementById("form-status").textContent.includes("Run complete"),null,{timeout:30000});
    assert.ok(await a.page.locator(".allocation-chart").count()>0,"Engine-backed allocation graphic missing");
    await a.page.locator('[data-preset="budget"]').click();
    assert.equal(await a.page.locator("#scenario-tools").isVisible(),false,"Stale result remained exportable");
    await a.page.locator("#run").click();
    await a.page.waitForFunction(() => document.getElementById("form-status").textContent.includes("Run complete"),null,{timeout:30000});
    assert.equal(await a.page.locator("#run-history li").count(),2);
    await a.page.locator("#run-history li").last().locator("button").click();
    assert.equal(await a.page.locator("#budget").inputValue(),"900000");
    assert.equal(await a.page.locator("#water").inputValue(),"10");
    assert.equal(await a.page.locator("#scenario-tools").isVisible(),false);
    await a.page.reload();
    await a.page.waitForFunction(() => document.getElementById("form-status").textContent.includes("Ready"));
    assert.equal(await a.page.locator("#run-history li").count(),1);
    assert.match(await a.page.locator("#run-history").innerText(),/Run the first scenario/);
    assert.deepEqual(a.thirdParty,[]);
    assert.deepEqual(a.errors,[]);
  } finally { await a.context.close(); }
});

test("P2 local export is evidence-bounded and mobile results reflow", async () => {
  const a=await openLab(320);
  try {
    await a.page.locator("#mode-expert").click();
    assert.equal(await a.page.locator("#mode-expert").getAttribute("aria-pressed"),"true");
    await a.page.locator('[data-preset="budget"]').click();
    await a.page.locator("#run").click();
    await a.page.waitForFunction(() => document.getElementById("form-status").textContent.includes("Run complete"),null,{timeout:30000});
    const downloadPromise=a.page.waitForEvent("download");
    await a.page.locator("#download-evidence").click();
    const download=await downloadPromise;
    assert.match(download.suggestedFilename(),/acecog-riverbend-experiment-v02\.json/);
    const fs=require("node:fs");
    const exportDoc=JSON.parse(fs.readFileSync(await download.path(),"utf8"));
    assert.equal(exportDoc.format,"ACECOG-LOCAL-EXPERIMENT-EVIDENCE-v0.2");
    assert.equal(exportDoc.scope,"FICTIONAL_LOCAL_ONLY_NO_LEGAL_EFFECT");
    assert.ok(exportDoc.alternative.chain_head);
    assert.equal(JSON.stringify(exportDoc).includes("X-Lab-Token"),false);
    await a.page.locator("#copy-recipe").click();
    await a.page.waitForFunction(() => /copied|Manual copy|unavailable/i.test(
      document.getElementById("export-status").textContent),null,{timeout:10000});
    const copyStatus=await a.page.locator("#export-status").innerText();
    assert.match(copyStatus,/copied|unavailable/i);
    if (/unavailable/i.test(copyStatus)) {
      assert.match(await a.page.locator("#recipe-fallback").inputValue(),/LOCAL-SCENARIO-RECIPE/);
    }
    await a.page.addScriptTag({path:require.resolve("axe-core/axe.min.js")});
    const ax=await a.page.evaluate(() => axe.run(document, {
      runOnly:{type:"tag",values:["wcag2a","wcag2aa","wcag21a","wcag21aa","wcag22aa"]}
    }));
    assert.deepEqual(ax.violations.map(v=>({id:v.id,nodes:v.nodes.map(n=>n.target)})),[]);
    const m=await a.page.evaluate(()=>({
      viewport:document.documentElement.clientWidth,
      scroll:document.documentElement.scrollWidth
    }));
    assert.ok(m.scroll<=m.viewport+1,"P2 root overflow: "+JSON.stringify(m));
    assert.deepEqual(a.thirdParty,[]);
    assert.deepEqual(a.errors,[]);
  } finally { await a.context.close(); }
});
