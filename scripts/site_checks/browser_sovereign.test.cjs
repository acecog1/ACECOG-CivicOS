// Actual browser WASM/Scipy feasibility check. Network only to local build host.
// Intentionally outside BG-1's immutable published-site test suite.
const { test } = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const { chromium } = require("playwright");

const base = process.env.ACECOG_BROWSER_BASE || "http://127.0.0.1:8781";

test("sovereign browser worker runs original CivicOS decision, solver and rejection", {timeout:180000}, async () => {
  const browser = await chromium.launch({headless:true});
  try {
    const context = await browser.newContext({viewport:{width:1280,height:900},serviceWorkers:"block",acceptDownloads:true});
    const page = await context.newPage();
    const outside=[], browserErrors=[];
    page.on("request",req=>{
      if (!req.url().startsWith(base+"/")) outside.push(req.url());
    });
    page.on("pageerror", e=>browserErrors.push(e.message));
    await page.goto(base+"/");
    await page.waitForFunction(()=>document.querySelector("#form-status")?.textContent.includes("Ready"),null,{timeout:20000});
    assert.match(await page.locator("h1").innerText(),/Scenario Laboratory/);
    await page.locator('[data-preset="votes"]').click();
    await page.locator("#run").click();
    // Cold-start WASM must lock every scenario-changing input; a slow
    // 30+ MB runtime load must never make a stale decision exportable.
    await page.waitForFunction(()=>
      document.querySelector("#lab-form")?.getAttribute("aria-busy")==="true",
      null,{timeout:15000});
    assert.equal(await page.locator("#budget").isDisabled(),true);
    assert.equal(await page.locator("#water").isDisabled(),true);
    assert.equal(await page.locator("#random").isDisabled(),true);
    assert.equal(await page.locator('[data-preset="budget"]').isDisabled(),true);
    assert.equal(await page.locator('input[name="vote-cara"]').first().isDisabled(),true);
    await page.waitForFunction(()=>/Run complete|unavailable/i.test(
      document.getElementById("form-status")?.textContent),null,{timeout:140000});
    const status=await page.locator("#form-status").innerText();
    assert.match(status,/Run complete/,status);
    await page.waitForFunction(() => document.querySelector("#budget")?.disabled === false);
    assert.equal(await page.locator("#random").isEnabled(),true);
    assert.equal(await page.locator("#scenario-tools").isVisible(),true);
    const content=await page.locator("#results").innerText();
    assert.match(content,/Plan A approved/);
    assert.match(content,/Plan A rejected/);
    assert.match(content,/No Plan A optimization, baseline or synthetic funding commitment/);
    const downloadPromise=page.waitForEvent("download");
    await page.locator("#download-evidence").click();
    const download=await downloadPromise;
    const record=JSON.parse(fs.readFileSync(await download.path(),"utf8"));
    const origin=record.provenance;
    assert.match(origin.source_manifest_sha256,/^[a-f0-9]{64}$/);
    assert.match(origin.runtime_manifest_sha256,/^[a-f0-9]{64}$/);
    assert.match(origin.pyodide_version,/^314[.]0[.]7$/);
    assert.match(origin.scipy_version,/^[0-9]+[.][0-9]+/);
    assert.equal(origin.raw_chain_events_included,false);
    assert.equal(origin.independent_verifier_included,false);
    assert.equal(origin.user_generated_content_is_authentic,false);
    assert.equal(origin.core_root_status,"EXACT_PINSET_VERIFIED_PENDING_INDEPENDENT_QA");
    assert.equal(record.browser_runtime.source_manifest_sha256,origin.source_manifest_sha256);
    assert.equal(outside.length,0,"Third-party network requests: "+outside.join(", "));
    assert.deepEqual(browserErrors,[]);
    await context.close();
  } finally {
    await browser.close();
  }
});

test("same-browser deterministic seeds and full native-vs-WASM funded portfolio parity", {timeout:180000}, async () => {
  const browser=await chromium.launch({headless:true});
  try {
    const context=await browser.newContext({viewport:{width:390,height:850},serviceWorkers:"block"});
    const page=await context.newPage();
    const outside=[];
    context.on("request",req=>{
      if (!req.url().startsWith(base+"/")) outside.push(req.url());
    });
    await page.goto(base+"/");
    await page.waitForFunction(()=>document.querySelector("#form-status")?.textContent.includes("Ready"),null,{timeout:20000});
    const observed=await page.evaluate(async ()=>{
      const a=await window.AcecogBrowserLab.fetch("/api/random?seed=42");
      const b=await window.AcecogBrowserLab.fetch("/api/random?seed=42");
      const input={
        budget:600000,water:12,crew:20,appropriation:350000,
        votes:{ana:"yes",ben:"yes",cara:"yes",dev:"yes",fay:"no"}
      };
      const out=await window.AcecogBrowserLab.fetch("/api/compare",{
        method:"POST",body:JSON.stringify(input)
      });
      const repeat=await window.AcecogBrowserLab.fetch("/api/compare",{
        method:"POST",body:JSON.stringify(input)
      });
      return {
        randA:await a.json(),randB:await b.json(),
        status:out.status,repeatedStatus:repeat.status,
        run:await out.json(),repeat:await repeat.json()
      };
    });
    assert.deepEqual(observed.randA,observed.randB,"Same seed must reproduce inputs");
    assert.equal(observed.status,200);
    assert.equal(observed.repeatedStatus,200);
    assert.equal(observed.run.alternative.chain_head,observed.repeat.alternative.chain_head,
      "Identical browser build and inputs must replay deterministically");
    assert.equal(observed.run.alternative.optimization.result_hash,
      observed.repeat.alternative.optimization.result_hash);
    assert.equal(observed.run.alternative.browser_runtime,undefined);
    assert.equal(observed.run.browser_runtime.mode,"client-only");
    assert.match(observed.run.browser_runtime.source_manifest_sha256,/^[0-9a-f]{64}$/);
    assert.match(observed.run.browser_runtime.runtime_manifest_sha256,/^[0-9a-f]{64}$/);
    assert.equal(observed.run.browser_runtime.core_root_release_attestation,"NOT_INDEPENDENTLY_APPROVED");
    assert.equal(observed.run.browser_runtime.independently_authenticated,false);
    assert.match(observed.run.browser_runtime.scipy,/^\d+\.\d+\.\d+/);
    assert.equal(observed.run.reference.decision.result,"approved");
    assert.equal(observed.run.alternative.decision.result,"approved");
    // Never ship the native test fixture in the reviewed/public WASM ZIP.
    // Load the independently generated baseline from test-runner disk only.
    const fixture=path.resolve(__dirname,"../../build/browser-lab/native-parity-golden.json");
    const native=JSON.parse(fs.readFileSync(fixture,"utf8"));
    assert.deepEqual(observed.run.alternative.decision.result,native.alternative.decision.result);
    assert.deepEqual(observed.run.alternative.portfolio_adopted,native.alternative.portfolio_adopted);
    assert.deepEqual(observed.run.alternative.baseline_created,native.alternative.baseline_created);
    assert.deepEqual(observed.run.alternative.synthetic_commitment_created,
      native.alternative.synthetic_commitment_created);
    const wasmAmounts=observed.run.alternative.optimization.solution.allocations;
    const nativeAmounts=native.alternative.optimization.solution.allocations;
    assert.deepEqual(Object.keys(wasmAmounts).sort(),Object.keys(nativeAmounts).sort());
    for (const id of Object.keys(nativeAmounts)) {
      assert.ok(Math.abs(wasmAmounts[id]-nativeAmounts[id]) <= 0.01,
        "SciPy WASM/native allocation parity mismatch for "+id+": "+wasmAmounts[id]+" vs "+nativeAmounts[id]);
    }
    const overflow=await page.evaluate(()=>document.documentElement.scrollWidth-
      document.documentElement.clientWidth);
    assert.ok(overflow<=1,"Unexpected mobile root overflow: "+overflow);
    assert.deepEqual(outside,[]);
    await context.close();
  } finally {
    await browser.close();
  }
});
