// Executes the ORIGINAL Python civic engine in a dedicated browser worker.
// The runtime, SciPy, JSON Schema dependencies and civic source are served
// by the same static host. No CDN fallback, user-authored Python or network API.
const BASE = new URL("./", import.meta.url);
const RUNTIME_BASE = new URL("./vendor/pyodide/", BASE);
const SOURCE_FILES = [
  "python/src/acecog/__init__.py",
  "python/src/acecog/engine.py",
  "python/src/acecog/contract.py",
  "python/scripts/experiment_riverbend.py",
  "python/tests/scenario.py"
];
let pyReady = null;

async function sourceWithHash(path, manifest) {
  if (!(path in manifest.files)) throw new Error("Unapproved Python module");
  const response = await fetch(new URL(path, BASE), {cache:"no-store"});
  if (!response.ok) throw new Error("Local Python module unavailable");
  const content = new Uint8Array(await response.arrayBuffer());
  const digest = await crypto.subtle.digest("SHA-256", content);
  const hash = Array.from(new Uint8Array(digest), b => b.toString(16).padStart(2,"0")).join("");
  if (hash !== manifest.files[path]) throw new Error("Engine bundle hash mismatch");
  return content;
}

async function initialize() {
  const manifestResponse = await fetch(new URL("source-manifest.json",BASE), {cache:"no-store"});
  if (!manifestResponse.ok) throw new Error("Source manifest absent");
  const manifest = await manifestResponse.json();
  if (manifest.schema !== "ACECOG-browser-lab-source-v0.1" ||
      manifest.scenario_kind !== "abbreviated-isolated-synthetic-not-279-event-fork") {
    throw new Error("Invalid browser source scope");
  }
  const {loadPyodide} = await import(new URL("pyodide.mjs", RUNTIME_BASE));
  const py = await loadPyodide({
    indexURL:RUNTIME_BASE.href,
    packageBaseUrl:RUNTIME_BASE.href
  });
  await py.loadPackage(["numpy","scipy","jsonschema"]);
  py.FS.mkdirTree("/acecog/src/acecog");
  py.FS.mkdirTree("/acecog/scripts");
  py.FS.mkdirTree("/acecog/tests");
  for (const relativePath of SOURCE_FILES) {
    const bytes = await sourceWithHash(relativePath,manifest);
    py.FS.writeFile("/acecog/" + relativePath.replace("python/",""), bytes);
  }
  // Import our untouched governance and optimized scenario routines, not a JS replica.
  py.runPython("import sys; sys.path.insert(0, '/acecog/src'); sys.path.insert(0, '/acecog/tests'); sys.path.insert(0, '/acecog/scripts'); import experiment_riverbend as lab");
  // Fingerprints identify the solver; never assert cross-build byte-for-byte parity
  // merely because the same source and scenario were used.
  const versions = py.runPython("import scipy, numpy, jsonschema; (scipy.__version__, numpy.__version__)").toJs();
  return {py,versions};
}
function ready() {
  if (!pyReady) pyReady = initialize().catch(error=>{pyReady=null; throw error;});
  return pyReady;
}
async function run(method,payload) {
  if (!["compare","random"].includes(method)) throw new Error("Unsupported calculation");
  const {py,versions} = await ready();
  if (method==="random") {
    if (!Number.isSafeInteger(payload) || payload<0 || payload>4294967295)
      throw new Error("Bad input seed");
    py.globals.set("_acecog_js_input", payload);
    return JSON.parse(py.runPython("import json; json.dumps(lab.surprise(_acecog_js_input), allow_nan=False)"));
  }
  if (!payload || typeof payload!=="object" || Array.isArray(payload))
    throw new Error("Inputs required");
  const clean = JSON.stringify(payload);
  if (clean.length>4096) throw new Error("Scenario too large");
  py.globals.set("_acecog_js_input",clean);
  const raw = await py.runPythonAsync("import json; json.dumps(lab.compare(json.loads(_acecog_js_input)), allow_nan=False)");
  const result = JSON.parse(raw);
  result.browser_runtime = {
    mode:"client-only",
    source_revision:"bundle-manifest",
    python:"Pyodide",
    scipy:versions[0],
    numpy:versions[1],
    limitation:"Fictional shortened fixture, not the 279-event published snapshot",
    network_compute:false
  };
  return result;
}
self.addEventListener("message", async event => {
  const {id,method,payload} = event.data || {};
  if (!Number.isSafeInteger(id)) return;
  try {
    self.postMessage({id,result:await run(method,payload)});
  } catch (_error) {
    self.postMessage({id,error:"Local Pyodide/SciPy calculation failed or required static files were unavailable"});
  }
});
