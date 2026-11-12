// BG2-R2: cross-engine browser qualification, not a native Safari/AT certificate.
// Operates on the independent, hash-verified, extracted review ZIP only.
"use strict";
const {test}=require("node:test");
const assert=require("node:assert/strict");
const fs=require("node:fs");
const {chromium,firefox,webkit}=require("playwright");

const engineName=process.env.BG2_BROWSER || "chromium";
const engine={chromium,firefox,webkit}[engineName];
if(!engine) throw Error("Unknown browser engine");
const base=process.env.ACECOG_BROWSER_BASE || "http://127.0.0.1:8781";
const output=process.env.BG2_QUAL_REPORT || "";
const axePath=require.resolve("axe-core");

test("BG2-R2 "+engineName+": sovereign scenario, busy race, export, mobile, accessibility proxy", {timeout:290000}, async()=>{
  const browser=await engine.launch({headless:true});
  const ctx=await browser.newContext({
    viewport:{width:320,height:800},acceptDownloads:true,serviceWorkers:"block"
  });
  await ctx.addInitScript({path:axePath});
  const page=await ctx.newPage();
  const unexpected=[],errors=[],responses=[];
  const t0=Date.now();
  let firstSolveMs=null;
  page.on("pageerror",e=>errors.push(String(e.message)));
  page.on("request",r=>{if(!r.url().startsWith(base+"/"))unexpected.push(r.url());});
  page.on("response",async r=>{
    if(r.url().startsWith(base+"/")){
      const headers=await r.allHeaders();
      const size=Number(headers["content-length"]||0);
      responses.push({path:new URL(r.url()).pathname,status:r.status(),
                      bytes:Number.isSafeInteger(size)?size:0});
    }
  });
  try{
    await page.goto(base+"/",{waitUntil:"domcontentloaded"});
    await page.waitForFunction(()=>document.querySelector("#form-status")?.textContent.includes("Ready"),null,{timeout:25000});
    assert.match(await page.locator("h1").innerText(),/Scenario Laboratory/);
    assert.equal((await page.locator("#lab-form").getAttribute("aria-busy")),null);
    const skip=page.locator('a.skip-link');
    assert.equal(await skip.getAttribute("href"),"#main");
    await page.keyboard.press("Tab");
    const focus=await page.evaluate(()=>document.activeElement?.tagName);
    assert.ok(["A","BUTTON","INPUT"].includes(focus),"Keyboard navigation should reach controls");
    const rootOverflow=await page.evaluate(
      ()=>document.documentElement.scrollWidth-document.documentElement.clientWidth);
    assert.ok(rootOverflow<=1,"320px root overflow: "+rootOverflow);

    // Cold worker load gives time to force an illegal DOM input edit. A stale
    // result must be discarded even if a script bypasses disabled controls.
    await page.locator('[data-preset="votes"]').click();
    await page.locator("#run").click();
    await page.waitForFunction(()=>document.querySelector("#lab-form")?.getAttribute("aria-busy")==="true",null,{timeout:15000});
    assert.equal(await page.locator("#budget").isDisabled(),true);
    assert.equal(await page.locator("#random").isDisabled(),true);
    assert.equal(await page.locator('[data-preset="water"]').isDisabled(),true);
    await page.evaluate(()=>{
      const input=document.querySelector("#budget");input.value="600000";
      input.dispatchEvent(new Event("input",{bubbles:true}));
    });
    await page.waitForFunction(()=>/Older result discarded|calculation failed|unavailable/i.test(
      document.querySelector("#form-status")?.textContent||""),null,{timeout:210000});
    const outcome=await page.locator("#form-status").innerText();
    assert.match(outcome,/Older result discarded/,outcome);
    assert.equal(await page.locator("#budget").isEnabled(),true);
    assert.equal(await page.locator("#scenario-tools").isVisible(),false);
    firstSolveMs=Date.now()-t0;

    // Second invocation uses the initialized local runtime; confirm the
    // rejection really prevents fictional authorizations and exposes export.
    await page.locator('[data-preset="votes"]').click();
    await page.locator("#run").click();
    await page.waitForFunction(()=>/Run complete|unavailable/i.test(
      document.querySelector("#form-status")?.textContent||""),null,{timeout:120000});
    assert.match(await page.locator("#form-status").innerText(),/Run complete/);
    const content=await page.locator("#results").innerText();
    assert.match(content,/Plan A rejected/);
    assert.match(content,/No Plan A optimization, baseline or synthetic funding commitment/);
    const downloadEvt=page.waitForEvent("download",{timeout:12000});
    await page.locator("#download-evidence").click();
    const downloaded=await downloadEvt;
    const evidence=JSON.parse(fs.readFileSync(await downloaded.path(),"utf8"));
    assert.equal(evidence.provenance.user_generated_content_is_authentic,false);
    assert.equal(evidence.provenance.raw_chain_events_included,false);
    assert.equal(evidence.provenance.independent_verifier_included,false);

    await page.locator("#random").click();
    await page.waitForFunction(()=>/New reproducible inputs selected|unavailable/i.test(
      document.querySelector("#form-status")?.textContent||""),null,{timeout:40000});
    assert.match(await page.locator("#form-status").innerText(),/New reproducible inputs selected/);
    assert.match(await page.locator("#seed-info").innerText(),/Random input seed:/);

    // This is ONLY a CSS-zoom/layout proxy. It cannot establish actual 200%
    // native browser zoom or VoiceOver/NVDA/JAWS behavior.
    await page.setViewportSize({width:1280,height:850});
    await page.evaluate(()=>{document.documentElement.style.zoom="200%";});
    const zoomOverflow=await page.evaluate(
      ()=>document.documentElement.scrollWidth-document.documentElement.clientWidth);
    assert.ok(zoomOverflow<=1,"200% CSS zoom proxy root overflow: "+zoomOverflow);

    const axe=await page.evaluate(async()=>{
      if(typeof window.axe==="undefined")return {missing:true};
      return await window.axe.run(document,{runOnly:{type:"tag",values:["wcag2a","wcag2aa","wcag21aa"]}});
    });
    assert.ok(!axe.missing,"Automated accessibility engine not loaded");
    const critical=axe.violations.filter(v=>["critical","serious"].includes(v.impact));
    assert.equal(critical.length,0,"Critical/serious axe violations "+JSON.stringify(
      critical.map(v=>({id:v.id,impact:v.impact,nodes:v.nodes.length}))));
    assert.deepEqual(unexpected,[],"No third-party runtime network calls");
    assert.deepEqual(errors,[],"Unexpected browser JS errors");

    const report={
      schema:"BG2-R2-QUALIFICATION-v1",engine:engineName,
      kind:engineName==="webkit"?"Playwright Linux WebKit, NOT native macOS Safari":engineName,
      viewport_px:320,zoom:"200% CSS zoom layout proxy; native 200% unverified",
      true_native_screen_reader:"NOT_PERFORMED",
      peak_browser_or_WASM_memory:"NOT_MEASURED",
      first_cold_worker_stale_result_ms:firstSolveMs,
      total_review_test_ms:Date.now()-t0,
      responses,
      total_content_length_bytes:responses.reduce((a,b)=>a+b.bytes,0),
      third_party_requests:unexpected,
      axe_critical_or_serious:critical.length,
      axe_incomplete:axe.incomplete?.length||0,
      detected_browser_js_errors:errors,
      result:"AUTOMATED_PASS_NOT_PUBLICATION_GO"
    };
    if(output){fs.mkdirSync(require("node:path").dirname(output),{recursive:true});
      fs.writeFileSync(output,JSON.stringify(report,null,2)+"\n");}
    console.log("BG2-R2-QUALIFICATION "+JSON.stringify(report));
  }finally{await ctx.close();await browser.close();}
});
