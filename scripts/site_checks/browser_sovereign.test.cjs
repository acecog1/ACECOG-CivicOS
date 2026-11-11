// Actual browser WASM/Scipy feasibility check. Network only to local build host.
// Intentionally outside BG-1's immutable published-site test suite.
const { test } = require("node:test");
const assert = require("node:assert/strict");
const { chromium } = require("playwright");

const base = process.env.ACECOG_BROWSER_BASE || "http://127.0.0.1:8781";

test("sovereign browser worker runs original CivicOS decision, solver and rejection", {timeout:180000}, async () => {
  const browser = await chromium.launch({headless:true});
  try {
    const context = await browser.newContext({viewport:{width:1280,height:900},serviceWorkers:"block"});
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
    await page.waitForFunction(()=>/Run complete|unavailable/i.test(
      document.getElementById("form-status")?.textContent),null,{timeout:140000});
    const status=await page.locator("#form-status").innerText();
    assert.match(status,/Run complete/,status);
    const content=await page.locator("#results").innerText();
    assert.match(content,/Plan A approved/);
    assert.match(content,/Plan A rejected/);
    assert.match(content,/No Plan A optimization, baseline or synthetic funding commitment/);
    assert.equal(outside.length,0,"Third-party network requests: "+outside.join(", "));
    assert.deepEqual(browserErrors,[]);
    await context.close();
  } finally {
    await browser.close();
  }
});
