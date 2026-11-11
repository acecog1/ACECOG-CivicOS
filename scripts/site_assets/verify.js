// Re-check the Riverbend record in the visitor's browser: hash = SHA-256(previous hash + event text).
// Fetches the static events.json; verification results stay local. Hosting requests still occur.
(function () {
  const strips = document.querySelectorAll("[data-chain]");
  if (!strips.length) return;
  if (!(window.crypto && crypto.subtle)) {
    for (const el of strips) el.querySelector('.chain-status').textContent =
      'Verification unavailable: this browser needs a secure context with SHA-256 support.';
    return;
  }
  const calm = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const enc = new TextEncoder();
  const hex = (buf) => Array.from(new Uint8Array(buf), (b) => b.toString(16).padStart(2, "0")).join("");
  const sha = async (s) => hex(await crypto.subtle.digest("SHA-256", enc.encode(s)));
  const frame = () => new Promise((r) => requestAnimationFrame(r));

  async function check(rec, el, tamperAt) {
    const events = rec.events;
    const box = el.querySelector(".squares"), status = el.querySelector(".chain-status");
    box.innerHTML = "";
    const expectedCount = Number(document.body.dataset.expectedCount);
    const expectedHead = document.body.dataset.expectedHead;
    if (!Array.isArray(events) || !Number.isSafeInteger(expectedCount) || expectedCount < 1 ||
        events.length !== expectedCount || rec.event_count !== expectedCount ||
        !/^[a-f0-9]{64}$/.test(expectedHead || '') || rec.chain_head !== expectedHead) {
      status.textContent = 'Record verification failed: count or fingerprint does not match this release.';
      return false;
    }
    const sq = events.map(() => box.appendChild(document.createElement("i")));
    status.textContent = `Checking ${events.length} records…`;
    let prev = "0".repeat(64);
    for (let i = 0; i < events.length; i++) {
      const ev = events[i];
      if (!ev || ev.seq !== i + 1 || typeof ev.text !== 'string' ||
          !/^[a-f0-9]{64}$/.test(ev.hash || '')) {
        status.textContent = 'Record verification failed: invalid record or sequence.';
        return false;
      }
      let text = ev.text;
      if (i === tamperAt) text = text.replace(/"amount":(\d)/, (m, d) => `"amount":${(Number(d) + 1) % 10}`).replace(/"at":"T\+/, '"at":"T+0');
      let linked = false;
      try {
        const parsed = JSON.parse(text);
        linked = parsed.prev_hash === prev && parsed.seq === ev.seq;
      } catch (e) { linked = false; }
      const h = await sha(prev + text);
      if (!linked || h !== ev.hash) {
        sq[i].className = "bad";
        for (let j = i + 1; j < sq.length; j++) sq[j].className = "after";
        status.innerHTML = `<strong>Record ${ev.seq} doesn't match its fingerprint.</strong> ` +
          `Every record after it is now unproven. This is what a rewritten history looks like.`;
        return false;
      }
      sq[i].className = "ok";
      prev = ev.hash;
      if (!calm && i % 6 === 5) await frame();
    }
    if (prev !== expectedHead) {
      status.textContent = 'Record verification failed: final fingerprint does not match this release.';
      return false;
    }
    status.innerHTML = `<strong>All ${events.length} records check out.</strong> ` +
      `The latest fingerprint is <code>${prev.slice(0, 16)}…</code>, and changing any earlier record would break it.`;
    return true;
  }

  fetch("events.json").then((r) => {
    if (!r.ok) throw new Error('record request failed');
    return r.json();
  }).then(async (rec) => {
    for (const el of strips) {
      const valid = await check(rec, el);
      const btn = document.querySelector("[data-tamper]");
      if (valid && btn && el.hasAttribute("data-full")) {
        btn.hidden = false;
        btn.addEventListener("click", async () => {
          btn.disabled = true;
          const k = Math.floor(rec.events.length * 0.4);
          await check(rec, el, k);
          btn.textContent = "Check the real record again";
          btn.disabled = false;
          btn.onclick = async (e) => { e.stopImmediatePropagation(); location.reload(); };
        }, { once: true });
      }
    }
  }).catch(() => {
    for (const el of strips) el.querySelector(".chain-status").textContent =
      "The record couldn't be loaded. Download events.json and check it with any SHA-256 tool.";
  });
})();
