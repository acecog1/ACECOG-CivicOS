"use strict";
// Development-only, same-origin client. No external scripts, cookies or analytics.
(function () {
  const $ = (id) => document.getElementById(id);
  const fields = ["budget", "water", "crew", "appropriation"];
  const displayNames = {ana:"Ana",ben:"Ben",cara:"Cara",dev:"Dev",eli:"Eli",fay:"Fay"};
  let config = null;
  let lastSeed = null;

  function add(tag, parent, text, cls) {
    const el = document.createElement(tag);
    if (cls) el.className = cls;
    if (text !== undefined && text !== null) el.textContent = String(text);
    parent.appendChild(el);
    return el;
  }

  function setStatus(message, error) {
    $("form-status").textContent = message;
    $("form-status").className = error ? "status-error" : "subtle";
  }

  function votesFromForm() {
    const result = {};
    config.voters.forEach((actor) => {
      const chosen = document.querySelector('input[name="vote-' + actor + '"]:checked');
      if (!chosen) throw new Error("No vote selected for " + actor);
      result[actor] = chosen.value;
    });
    return result;
  }

  function parametersFromForm() {
    const p = {};
    fields.forEach((name) => {
      const str = $(name).value;
      const n = Number(str);
      const limits = config.constraints[name];
      if (str === "" || !Number.isSafeInteger(n) || n < limits[0] || n > limits[1]) {
        throw new Error("Invalid " + name + " input");
      }
      p[name] = n;
    });
    p.votes = votesFromForm();
    return p;
  }

  function configureVotes() {
    const host = $("vote-controls");
    host.replaceChildren();
    config.voters.forEach((actor) => {
      const row = add("div", host, null, "vote-row");
      add("span", row, displayNames[actor] || actor, "vote-name");
      const options = add("div", row, null, "vote-options");
      ["yes", "no", "abstain"].forEach((choice) => {
        const label = add("label", options, null, "vote-choice");
        const input = add("input", label);
        input.type = "radio";
        input.name = "vote-" + actor;
        input.value = choice;
        input.checked = config.defaults.votes[actor] === choice;
        add("span", label, choice.charAt(0).toUpperCase() + choice.slice(1));
      });
    });
    const row = add("div", host, null, "vote-row");
    add("span", row, displayNames[config.recused] || config.recused, "vote-name");
    add("span", row, "Recused — voting prohibited", "recused");
  }

  function updateInputs(p) {
    fields.forEach((name) => { $(name).value = p[name]; });
    config.voters.forEach((actor) => {
      const choice = p.votes[actor];
      const el = document.querySelector('input[name="vote-' + actor + '"][value="' + choice + '"]');
      if (el) el.checked = true;
    });
  }

  function money(v) {
    return "$" + Number(v).toLocaleString("en-US", {maximumFractionDigits: 2});
  }

  function showDecision(parent, title, data) {
    const box = add("section", parent, null, "decision");
    add("h3", box, title);
    const result = data.decision.result;
    add("p", box, result === "approved" ? "Plan A approved" : "Plan A rejected",
        result === "approved" ? "decision-yes" : "decision-no");
    const choices = data.decision.tally.choices;
    add("p", box, String(choices.yes || 0) + " yes · " + String(choices.no || 0) +
        " no · " + String(choices.abstain || 0) + " abstain");
    add("p", box, "Portfolio adopted: " + (data.portfolio_adopted ? "Yes" : "No"));
    const solution = data.optimization && data.optimization.solution;
    if (solution) {
      add("p", box, "Synthetic allocation: " +
          money(Object.values(solution.allocations).reduce((acc, amount) => acc + amount, 0)));
      add("p", box, "Binding limits: " +
          (solution.binding_constraints.length ? solution.binding_constraints.join(", ") : "none"));
    } else {
      add("p", box, "No authorized optimized portfolio allocation in this branch.");
    }
    add("p", box, "Chain " + data.chain_head.slice(0, 16) + "… · " +
        data.event_count + " records", "hash");
    return box;
  }

  function showAllocations(parent, base, alt) {
    const b = base.optimization && base.optimization.solution;
    const a = alt.optimization && alt.optimization.solution;
    if (!a && !b) return;
    add("h3", parent, "Initiative funding comparison");
    const wrapper = add("div", parent, null, "table-wrap");
    wrapper.tabIndex = 0;
    wrapper.setAttribute("aria-label", "Scroll horizontally to inspect project allocations");
    const table = add("table", wrapper);
    const caption = add("caption", table, "Dollar allocations from the CivicOS optimization engine");
    caption.className = "subtle";
    const thead = add("thead", table);
    const head = add("tr", thead);
    ["Project ID", "Reference", "Alternative", "Change"].forEach((v) => add("th", head, v));
    const tbody = add("tbody", table);
    const ids = Object.keys((b && b.allocations) || (a && a.allocations) || {});
    ids.forEach((id) => {
      const before = b ? b.allocations[id] : null;
      const after = a ? a.allocations[id] : null;
      const tr = add("tr", tbody);
      add("th", tr, id);
      add("td", tr, before === null ? "Not authorized" : money(before));
      add("td", tr, after === null ? "Not authorized" : money(after));
      add("td", tr, before === null || after === null ? "—" : money(after - before));
    });
  }

  function showResult(payload) {
    const root = $("results");
    root.replaceChildren();
    const both = add("div", root, null, "comparison");
    showDecision(both, "Reference", payload.reference);
    showDecision(both, "Your alternative", payload.alternative);
    const narrative = add("section", root);
    add("h3", narrative, "What changed—and what remains unknown");
    const ul = add("ul", narrative, null, "narrative");
    payload.impact_narrative.statements.forEach((line) => add("li", ul, line));
    showAllocations(root, payload.reference, payload.alternative);
    const evidence = add("details", root);
    add("summary", evidence, "View verification and reproduction evidence");
    const pre = add("pre", evidence, null, "evidence");
    pre.textContent = JSON.stringify({
      reference_inputs: payload.reference.inputs,
      alternative_inputs: payload.alternative.inputs,
      reference_chain_head: payload.reference.chain_head,
      alternative_chain_head: payload.alternative.chain_head,
      original_replay: payload.reference.replay || null,
      alternative_replay: payload.alternative.replay || null,
      explanation_basis: payload.impact_narrative.method
    }, null, 2);
    add("p", root, payload.warning, "warning");
  }

  async function request(url, options) {
    const response = await fetch(url, Object.assign({cache:"no-store"}, options || {}));
    const body = await response.json();
    if (!response.ok) throw new Error(body.error || ("HTTP " + response.status));
    return body;
  }

  async function run(evt) {
    if (evt) evt.preventDefault();
    if (!config) return;
    try {
      const params = parametersFromForm();
      setStatus("Computing two independent CivicOS branches…", false);
      $("run").disabled = true;
      const result = await request("/api/compare", {
        method:"POST",
        headers:{"Content-Type":"application/json","X-Lab-Token":config.token},
        body:JSON.stringify(params)
      });
      showResult(result);
      setStatus("Run complete. No public records or real civic actions were changed.", false);
    } catch (err) {
      setStatus(err.message || "The local simulation failed.", true);
    } finally {
      $("run").disabled = false;
    }
  }

  async function randomize() {
    if (!config) return;
    try {
      const bytes = new Uint32Array(1);
      crypto.getRandomValues(bytes);
      lastSeed = bytes[0];
      const data = await request("/api/random?seed=" + encodeURIComponent(String(lastSeed)));
      updateInputs(data.parameters);
      $("seed-info").textContent = "Random input seed: " + String(lastSeed) +
        ". Select Run to compute the effect; the solver itself remains deterministic.";
      setStatus("New reproducible inputs selected, not yet run.", false);
    } catch (err) { setStatus(err.message, true); }
  }

  async function main() {
    try {
      config = await request("/api/config");
      configureVotes();
      updateInputs(config.defaults);
      setStatus("Ready. Change variables, change votes, then run the engine.", false);
      $("lab-form").addEventListener("submit", run);
      $("random").addEventListener("click", randomize);
      $("reset").addEventListener("click", function () {
        updateInputs(config.defaults);
        lastSeed = null;
        $("seed-info").textContent = "";
        setStatus("Reference assumptions restored. Select Run to compare again.", false);
      });
    } catch (err) {
      setStatus("Local engine unavailable: " + err.message, true);
      $("run").disabled = true;
    }
  }
  main();
}());
