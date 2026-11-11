"use strict";
// P2: Guided visitor layer. All scenarios use the existing local CivicOS engine.
// No storage, cookies, analytics, third-party services, or public share links.
(function () {
  const $ = id => document.getElementById(id);
  const numeric = ["budget", "water", "crew", "appropriation"];
  const defaultVotes = {ana:"yes",ben:"yes",cara:"yes",dev:"yes",fay:"no"};
  const defaults = {budget:900000,water:20,crew:30,appropriation:650000,votes:defaultVotes};
  const presets = {
    water: {budget:900000,water:10,crew:18,appropriation:650000,votes:defaultVotes,
      explanation:"Water is now limited to 10 ML/year and crew capacity to 18 crew-weeks. Run the engine to see whether the portfolio can adapt."},
    budget: {budget:600000,water:20,crew:30,appropriation:350000,votes:defaultVotes,
      explanation:"The investment budget is now $600,000 and non-grant appropriations are capped at $350,000. Run to inspect the actual allocations."},
    votes: {budget:900000,water:20,crew:30,appropriation:650000,votes:{ana:"yes",ben:"yes",cara:"no",dev:"no",fay:"no"},
      explanation:"Cara and Dev now vote no. If Plan A is rejected, the engine cannot authorize its downstream portfolio or synthetic funding."}
  };
  let recent = [];
  let latest = null;

  function applyInputs(p) {
    numeric.forEach(field => { $(field).value = String(p[field]); });
    for (const [actor, choice] of Object.entries(p.votes)) {
      const radio = document.querySelector('input[name="vote-' + actor + '"][value="' + choice + '"]');
      if (radio) radio.checked = true;
    }
  }
  function inputSummary(p) {
    const v=p.votes;
    const yes=Object.values(v).filter(x=>x==="yes").length;
    const no=Object.values(v).filter(x=>x==="no").length;
    return "$"+Number(p.budget).toLocaleString("en-US")+" budget · "+p.water+
      " ML/year · "+yes+" yes / "+no+" no";
  }
  function expireViewedResult() {
    if (!latest) return;
    latest = null;
    $("scenario-tools").hidden=true;
    $("export-status").textContent="";
    $("recipe-fallback").hidden=true;
    $("recipe-fallback-label").hidden=true;
    $("results").replaceChildren();
    const p=document.createElement("p");
    p.className="subtle";
    p.textContent="Assumptions changed. Run the engine again to see an updated comparison; the prior results remain in your temporary history.";
    $("results").appendChild(p);
  }
  function clearSelectedPreset() {
    document.querySelectorAll("[data-preset]").forEach(b=>b.setAttribute("aria-pressed","false"));
  }
  function choosePreset(key) {
    if ($("lab-form").getAttribute("aria-busy")==="true") return;
    const p=presets[key];
    if (!p) return;
    applyInputs(p);
    document.dispatchEvent(new Event("acecog:inputs-changed"));
    expireViewedResult();
    clearSelectedPreset();
    document.querySelector('[data-preset="'+key+'"]').setAttribute("aria-pressed","true");
    $("scenario-description").textContent=p.explanation;
    $("form-status").textContent="Suggested assumptions applied. Select Run with CivicOS engine.";
    $("run").focus();
  }
  function renderRecent() {
    const host=$("run-history");
    host.replaceChildren();
    recent.forEach((item,index)=>{
      const li=document.createElement("li");
      const b=document.createElement("button");
      b.type="button";
      b.textContent="Restore run "+item.run+": "+item.status+" · "+inputSummary(item.inputs);
      b.addEventListener("click",()=>{
        if ($("lab-form").getAttribute("aria-busy")==="true") return;
        applyInputs(item.inputs);
        document.dispatchEvent(new Event("acecog:inputs-changed"));
        expireViewedResult();
        clearSelectedPreset();
        $("scenario-description").textContent="Restored inputs from run "+item.run+". Select Run to reproduce or adjust them.";
        $("form-status").textContent="Inputs restored from this visit's history; no previous output has been reauthorized.";
        $("run").focus();
      });
      li.appendChild(b);
      host.appendChild(li);
    });
  }
  function exportEvidence() {
    if (!latest) return;
    const record={
      format:"ACECOG-LOCAL-EXPERIMENT-EVIDENCE-v0.2",
      scope:"FICTIONAL_LOCAL_ONLY_NO_LEGAL_EFFECT",
      source_note:"Abbreviated synthetic Riverbend fixture; NOT a canonical 279-event fork",
      seed_last_selected:latest.seed,
      ...latest.payload,
      provenance:{
        source_checkout_revision:latest.payload.browser_runtime?.source_revision || "unrecorded-local-build",
        source_manifest_sha256:latest.payload.browser_runtime?.source_manifest_sha256 || null,
        runtime_manifest_sha256:latest.payload.browser_runtime?.runtime_manifest_sha256 || null,
        pyodide_version:latest.payload.browser_runtime?.pyodide_version || null,
        pyodide_root_lock_sha256:latest.payload.browser_runtime?.pyodide_root_lock_sha256 || null,
        scipy_version:latest.payload.browser_runtime?.scipy || null,
        numpy_version:latest.payload.browser_runtime?.numpy || null,
        core_root_status:latest.payload.browser_runtime?.core_root_status || "UNATTESTED",
        raw_chain_events_included:false,
        independent_verifier_included:false,
        user_generated_content_is_authentic:false,
        limitation:"Visitor-generated synthetic summaries are editable. Chain-head alone does not authenticate evidence; replay requires matching independent source/runtime and full event history."
      }
    };
    const blob=new Blob([JSON.stringify(record,null,2)+"\n"],{type:"application/json"});
    const url=URL.createObjectURL(blob);
    const link=document.createElement("a");
    link.href=url;
    link.download="acecog-riverbend-experiment-v02.json";
    document.body.appendChild(link);
    link.click();
    link.remove();
    URL.revokeObjectURL(url);
    $("export-status").textContent="Local evidence export prepared. Verify your browser download.";
  }
  async function copyRecipe() {
    if (!latest) return;
    const recipe=JSON.stringify({
      format:"ACECOG-LOCAL-SCENARIO-RECIPE-v0.2",
      limitation:"Synthetic fixture, not a shareable link or canonical Riverbend fork",
      assumptions:latest.payload.alternative.inputs,
      expected_chain_head:latest.payload.alternative.chain_head,
      source_checkout_revision:latest.payload.browser_runtime?.source_revision || "unrecorded-local-build",
      source_manifest_sha256:latest.payload.browser_runtime?.source_manifest_sha256 || null,
      runtime_manifest_sha256:latest.payload.browser_runtime?.runtime_manifest_sha256 || null,
      pyodide_version:latest.payload.browser_runtime?.pyodide_version || null,
      scipy_version:latest.payload.browser_runtime?.scipy || null,
      independent_authentication:false,
      notice:"Recipe is fictional, visitor-controlled and cannot authenticate a civic decision. Identical inputs may differ across scientific runtime versions."
    },null,2);
    try {
      if (!navigator.clipboard || !navigator.clipboard.writeText) throw new Error("Clipboard unavailable");
      await navigator.clipboard.writeText(recipe);
      $("export-status").textContent="Scenario recipe copied. Paste it into a file or message; no data was uploaded.";
      $("recipe-fallback").hidden=true;
      $("recipe-fallback-label").hidden=true;
    } catch (_) {
      $("recipe-fallback").value=recipe;
      $("recipe-fallback").hidden=false;
      $("recipe-fallback-label").hidden=false;
      $("recipe-fallback").focus();
      $("recipe-fallback").select();
      $("export-status").textContent="Clipboard access unavailable. Manually copy the recipe shown below.";
    }
  }
  // Hide prior exports immediately on new computation, and freeze history
  // restoration while busy. A later result event is the only unlock for export.
  document.addEventListener("acecog:busy",event=>{
    const working=event.detail.busy;
    if (working) expireViewedResult();
    document.querySelectorAll("#run-history button").forEach(button=>{
      button.disabled=working;
    });
  });
  document.addEventListener("acecog:result",event=>{
    const {payload,seed}=event.detail;
    latest={payload,seed:seed===null?null:seed};
    const status=payload.alternative.decision.result;
    const entry={run:recent.length?Math.max(...recent.map(r=>r.run))+1:1,
      status:"Plan A "+status,
      inputs:JSON.parse(JSON.stringify(payload.alternative.inputs))};
    recent.unshift(entry);
    // Count is monotonic in this tab, despite the bounded three-item history.
    if (recent.length>3) recent.length=3;
    renderRecent();
    document.querySelectorAll("#run-history button").forEach(button=>{
      button.disabled=$("lab-form").getAttribute("aria-busy")==="true";
    });
    $("scenario-tools").hidden=false;
    $("export-status").textContent="Results came from the local CivicOS engine. Export or copy deliberately; nothing was saved remotely.";
    $("scenario-description").textContent="Your scenario "+status+
      ". Review the evidence-grounded explanation and try another assumption.";
  });
  document.querySelectorAll("[data-preset]").forEach(button=>
    button.addEventListener("click",()=>choosePreset(button.dataset.preset)));
  $("mode-guided").addEventListener("click",()=>{
    $("mode-guided").setAttribute("aria-pressed","true");
    $("mode-expert").setAttribute("aria-pressed","false");
    $("mode-explanation").textContent="Guided: start with one change, run the engine, and compare the results. All controls remain available.";
  });
  $("mode-expert").addEventListener("click",()=>{
    $("mode-guided").setAttribute("aria-pressed","false");
    $("mode-expert").setAttribute("aria-pressed","true");
    $("mode-explanation").textContent="Detailed: adjust all numeric limits, inspect binding constraints and portfolio allocations, and open the evidence digests after running.";
  });
  $("lab-form").addEventListener("input",event=>{
    if (!event.target.matches("input")) return;
    expireViewedResult();
    clearSelectedPreset();
    $("scenario-description").textContent="Custom assumptions selected. Run the engine to learn what follows from your changes.";
  });
  $("lab-form").addEventListener("change",event=>{
    if (!event.target.matches("input")) return;
    expireViewedResult();
    clearSelectedPreset();
  });
  $("reset").addEventListener("click",()=>{
    expireViewedResult();
    clearSelectedPreset();
    $("scenario-description").textContent="Default assumptions restored. Run the engine to compare them.";
  });
  $("random").addEventListener("click",()=>{
    expireViewedResult();
    clearSelectedPreset();
    $("scenario-description").textContent="Surprise me is selecting a reproducible set of fictional assumptions. Run the engine after selection.";
  });
  $("download-evidence").addEventListener("click",exportEvidence);
  $("copy-recipe").addEventListener("click",copyRecipe);
}());
