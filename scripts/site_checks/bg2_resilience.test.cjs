// BG2-R2 bounded low-bandwidth and Worker failure/reload recovery check.
// Must run ONLY against the hash-verified extracted review ZIP on localhost.
const {test}=require("node:test");
const assert=require("node:assert/strict");
const fs=require("node:fs");
const {execFileSync}=require("node:child_process");
const {chromium}=require("playwright");
const base=process.env.ACECOG_BROWSER_BASE || "http://127.0.0.1:8781";
const reportPath=process.env.BG2_RESILIENCE_REPORT || "";
test("BG2-R2: rejected WASM fetch unlocks; reload recovers; throttled offline-free compute", {timeout:280000},async()=>{
  const browser=await chromium.launch({headless:true});
  let maxSampledRSSKB=0;
  const rss=()=>{try{
    const lines=execFileSync("ps",["-e","-o","comm=,rss="],
                            {encoding:"utf8",timeout:1800}).split("\n");
    const sum=lines.reduce((acc,line)=>{
      const match=line.trim().match(/^(.*\S)\s+(\d+)$/);
      return match&&/(chrome|chromium|firefox|WebKit|MiniBrowser|headless_shell)/i.test(match[1])
        ? acc+Number(match[2]):acc;
    },0);
    maxSampledRSSKB=Math.max(maxSampledRSSKB,sum);
  }catch(_e){}};
  const timer=setInterval(rss,350);
  const context=await browser.newContext({viewport:{width:390,height:800},serviceWorkers:"block"});
  const page=await context.newPage();
  const stray=[];
  page.on("request",r=>{if(!r.url().startsWith(base+"/"))stray.push(r.url());});
  let faultTriggered=false;
  const forbidden="**/vendor/pyodide/pyodide.asm.wasm";
  try{
    await context.route(forbidden,async route=>{
      if(!faultTriggered){faultTriggered=true;
        await route.fulfill({status:503,body:"injected worker-runtime failure"});}
      else await route.continue();
    });
    await page.goto(base+"/");
    await page.waitForFunction(()=>/Ready/.test(document.querySelector("#form-status")?.textContent||""));
    await page.locator("#run").click();
    await page.waitForFunction(()=>/failed|unavailable/i.test(
      document.querySelector("#form-status")?.textContent||""),null,{timeout:110000});
    assert.equal(faultTriggered,true,"WASM request failure path must have been exercised");
    assert.equal(await page.locator("#run").isEnabled(),true);
    assert.equal(await page.locator("#scenario-tools").isVisible(),false);
    await context.unroute(forbidden);

    // Explicit reload-based recovery; no unsupported claim of transparent
    // worker restart or persisted visitor experiment recovery.
    await page.reload();
    await page.waitForFunction(()=>/Ready/.test(document.querySelector("#form-status")?.textContent||""));
    await page.locator("#run").click();
    await page.waitForFunction(()=>/Run complete|unavailable/i.test(
      document.querySelector("#form-status")?.textContent||""),null,{timeout:120000});
    assert.match(await page.locator("#form-status").innerText(),/Run complete/);

    // Chromium CDP network throughput limit is a reproducible proxy for
    // constrained network. It is not a device-RAM or native mobile test.
    await page.close();
    const slow=await context.newPage();
    const cdp=await context.newCDPSession(slow);
    await cdp.send("Network.enable");
    await cdp.send("Performance.enable");
    await cdp.send("Network.emulateNetworkConditions",{
      offline:false,latency:125,
      downloadThroughput:1_500_000,
      uploadThroughput:100_000,
      connectionType:"cellular3g"
    });
    const start=Date.now();
    await slow.goto(base+"/",{waitUntil:"domcontentloaded"});
    await slow.waitForFunction(()=>/Ready/.test(document.querySelector("#form-status")?.textContent||""));
    await slow.locator("#run").click();
    await slow.waitForFunction(()=>/Run complete|unavailable/i.test(
      document.querySelector("#form-status")?.textContent||""),null,{timeout:190000});
    const elapsed=Date.now()-start;
    assert.match(await slow.locator("#form-status").innerText(),/Run complete/);
    const metrics=await cdp.send("Performance.getMetrics");
    const heap=metrics.metrics.find(x=>x.name==="JSHeapUsedSize")?.value??null;
    assert.deepEqual(stray,[]);
    rss();
    const receipt={
      schema:"BG2-R2-RESILIENCE-v1",
      platform:"headless Chromium on CI Linux, NOT a real low-RAM handset",
      worker_failure_injected_and_observed:faultTriggered,
      recovery:"successful after explicit reload, NOT automatically transparent",
      network_emulation:"125ms latency and 1,500,000 bytes/sec down",
      throttled_first_run_ms:elapsed,
      performance_warning_threshold_ms:30000,
      throttled_performance:elapsed>30000?"REQUIRES_PERFORMANCE_REVIEW":"UNDER_30_SECOND_PROXY",
      max_sampled_sum_browser_process_rss_kb:maxSampledRSSKB,
      memory_limit:"Summed process RSS is approximate and double-counts shared pages; NOT unique peak WASM memory",
      page_js_heap_used_bytes_snapshot:heap,
      external_network_requests:stray,
      result:"BROWSER_PROXY_EVIDENCE_ONLY_NOT_NATIVE_AT_OR_LOW_MEMORY_CERTIFICATION"
    };
    if(reportPath){const path=require("node:path");
      fs.mkdirSync(path.dirname(reportPath),{recursive:true});
      fs.writeFileSync(reportPath,JSON.stringify(receipt,null,2)+"\n");}
    console.log("BG2-R2-RESILIENCE "+JSON.stringify(receipt));
    await cdp.detach();
  }finally{clearInterval(timer);await context.close();await browser.close();}
});
