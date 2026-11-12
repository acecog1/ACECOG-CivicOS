"use strict";
// ACECOG browser-only adapter: intentionally no HTTP simulation service or storage.
// Existing P2 interface receives Response-compatible objects from a local Worker.
(function () {
  const DEFAULTS = {
    budget: 900000, water: 20, crew: 30, appropriation: 650000,
    votes: {ana: "yes", ben: "yes", cara: "yes", dev: "yes", fay: "no"}
  };
  const CONSTRAINTS = {
    budget:[400000,1400000],water:[5,40],crew:[10,50],appropriation:[250000,850000]
  };
  const config = {
    token: "not-an-authentication-token",
    defaults: DEFAULTS, constraints: CONSTRAINTS,
    voters: ["ana","ben","cara","dev","fay"],recused:"eli",
    disclaimer:"Browser-only fictional advisory laboratory, no legal effect or network compute API"
  };
  let worker = null;
  let nextId = 1;
  const pending = new Map();

  function reply(status, body) {
    return new Response(JSON.stringify(body), {
      status, headers: {"Content-Type":"application/json; charset=utf-8",
                        "Cache-Control":"no-store"}
    });
  }
  function stopWorker(message) {
    if (worker) worker.terminate();
    worker = null;
    for (const item of pending.values()) {
      clearTimeout(item.timeout);
      item.reject(new Error(message));
    }
    pending.clear();
  }
  function ensureWorker() {
    if (worker) return worker;
    if (typeof Worker !== "function") throw new Error("This browser does not support Web Workers.");
    worker = new Worker("./browser-engine-worker.mjs", {type:"module"});
    worker.addEventListener("message", event => {
      const {id, result, error} = event.data || {};
      const item = pending.get(id);
      if (!item) return;
      clearTimeout(item.timeout);
      pending.delete(id);
      if (error) item.reject(new Error("Local CivicOS computation unavailable: " + error));
      else item.resolve(result);
    });
    worker.addEventListener("error", () =>
      stopWorker("The local WebAssembly worker could not load. No run was published."));
    worker.addEventListener("messageerror", () =>
      stopWorker("Invalid local worker result."));
    return worker;
  }
  function askWorker(method, payload) {
    return new Promise((resolve,reject) => {
      const id = nextId++;
      let current;
      try { current = ensureWorker(); } catch(e) { reject(e); return; }
      const timeout = setTimeout(() => {
        stopWorker("The browser computation exceeded its time limit.");
      }, 90000); // Allows a cold, self-hosted WASM package load on slower devices.
      pending.set(id,{resolve,reject,timeout});
      current.postMessage({id,method,payload});
    });
  }
  async function fetchSimulation(url, options={}) {
    const path = new URL(url,location.href);
    if (path.origin !== location.origin ||
        !["/api/config","/api/random","/api/compare"].includes(path.pathname)) {
      return reply(404,{error:"Unsupported local simulation operation"});
    }
    if (path.pathname === "/api/config") return reply(200,config);
    try {
      if (path.pathname === "/api/random") {
        const seed = path.searchParams.get("seed");
        if (path.searchParams.size !== 1 || !/^\d{1,10}$/.test(seed || "") ||
            Number(seed) > 4294967295) return reply(400,{error:"Invalid random seed"});
        const parameters = await askWorker("random", Number(seed));
        return reply(200,{seed:Number(seed),parameters});
      }
      if ((options.method || "").toUpperCase() !== "POST") {
        return reply(405,{error:"Run requires a local POST-shaped message"});
      }
      const raw = options.body || "";
      if (typeof raw !== "string" || raw.length > 4096) {
        return reply(413,{error:"Scenario payload too large"});
      }
      const payload = JSON.parse(raw);
      if (!payload || typeof payload !== "object" || Array.isArray(payload) ||
          Object.keys(payload).some(k => !["budget","water","crew","appropriation","votes"].includes(k))) {
        return reply(400,{error:"Invalid synthetic input"});
      }
      return reply(200,await askWorker("compare",payload));
    } catch (_err) {
      // Never return internal Python exceptions or source data in public UI.
      return reply(503,{error:"Local browser engine unavailable; no scenario result was published."});
    }
  }

  window.AcecogBrowserLab = Object.freeze({fetch:fetchSimulation});
})();
