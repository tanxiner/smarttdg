import fs from "fs";
import path from "path";
import { chromium } from "playwright";
import { fileURLToPath } from "url";

function usage() {
    console.error("Usage: node render_mermaid_svg.mjs <input.mmd> <output.svg>");
    process.exit(2);
}

const inPath = process.argv[2];
const outPath = process.argv[3];
if (!inPath || !outPath) usage();

const code = fs.readFileSync(inPath, "utf8");

// Export-only config (frontend stays fast)
const exportConfig = {
    startOnLoad: false,
    theme: "default",
    securityLevel: "loose",
    maxTextSize: 1_000_000,
    maxEdges: 5000,
    flowchart: { htmlLabels: false }
};

console.log("Exporter maxTextSize =", exportConfig.maxTextSize);
console.log("Input length =", code.length);

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// ✅ Use single-file Mermaid build (no chunk imports)
const mermaidUmdPath = path.join(
    __dirname,
    "node_modules",
    "mermaid",
    "dist",
    "mermaid.min.js"
);

if (!fs.existsSync(mermaidUmdPath)) {
    console.error("Cannot find mermaid.min.js at:", mermaidUmdPath);
    process.exit(5);
}

const mermaidUmdCode = fs.readFileSync(mermaidUmdPath, "utf8");

// Build a self-contained HTML page
const html = `<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <style>
    body { margin: 0; padding: 0; background: transparent; }
    #wrap { padding: 8px; }
  </style>
</head>
<body>
  <div id="wrap"><div id="container"></div></div>

  <script>
    // Inject mermaid UMD/IIFE bundle
    ${mermaidUmdCode}

    const code = ${JSON.stringify(code)};
    const cfg = ${JSON.stringify(exportConfig)};

    (async () => {
      try {
        // mermaid is exposed globally by mermaid.min.js
        mermaid.initialize(cfg);

        const id = "export";
        const out = await mermaid.render(id, code);
        const svg = out.svg;

        const container = document.getElementById("container");
        container.innerHTML = svg;

        const el = container.querySelector("svg");
        if (el) {
          if (!el.getAttribute("viewBox")) {
            const w = (el.getAttribute("width") || "").replace("px","");
            const h = (el.getAttribute("height") || "").replace("px","");
            if (w && h) el.setAttribute("viewBox", "0 0 " + w + " " + h);
          }
          el.setAttribute("xmlns", "http://www.w3.org/2000/svg");
          el.style.background = "white";     // helps some viewers
          el.setAttribute("width", "2400");  // avoid width="100%" weirdness
        }

        window.__SVG__ = container.innerHTML;
      } catch (e) {
        window.__ERR__ = "ERR:" + String(e && e.stack ? e.stack : e);
      }
    })();
  </script>
</body>
</html>`;

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1400, height: 900 } });

page.on("console", (msg) => console.log("[PAGE]", msg.type(), msg.text()));
page.on("pageerror", (err) => console.error("[PAGEERROR]", err));

await page.setContent(html, { waitUntil: "domcontentloaded" });

const handle = await page.waitForFunction(() => {
    // eslint-disable-next-line no-undef
    return window.__SVG__ || window.__ERR__;
}, { timeout: 180_000 });

const val = await handle.jsonValue();
await browser.close();

if (typeof val === "string" && val.startsWith("ERR:")) {
    console.error(val);
    process.exit(4);
}

fs.writeFileSync(outPath, val, "utf8");
console.log("Wrote:", outPath);