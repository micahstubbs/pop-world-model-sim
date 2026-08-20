#!/usr/bin/env node
// Generates the popsim favicon set from one parametric SVG: a 3x3 population
// dot grid on the site's ink background — seven amber personas plus one
// positive (teal) and one negative (orange) sentiment accent, echoing the
// site's --amber1/--pos/--neg palette. Outputs: site/favicon.svg,
// site/favicon.ico (48/32/16), site/icons/apple-touch-icon.png.
// Requires inkscape + ImageMagick `convert`.
import { execFileSync } from "node:child_process";
import { mkdtempSync, writeFileSync, mkdirSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const INK = "#16130f";
const AMBER = "#e5a94d";
const POS = "#2ea88f";
const NEG = "#e06a44";

// 3x3 grid in a 512 box; `inset` pulls the grid toward center (apple-touch
// renders full-bleed with no rounded mask of its own, so it gets more air).
function svg({ rx, inset }) {
  const positions = [118, 256, 394].map((v) => {
    const t = (v - 256) * (1 - inset) + 256;
    return Math.round(t * 10) / 10;
  });
  const r = Math.round(52 * (1 - inset * 0.4) * 10) / 10;
  // Row-major colors: one pos accent (middle-right), one neg (bottom-left).
  const colors = [
    AMBER, AMBER, AMBER,
    AMBER, AMBER, POS,
    NEG, AMBER, AMBER,
  ];
  const dots = positions
    .flatMap((cy, row) => positions.map((cx, col) => ({ cx, cy, fill: colors[row * 3 + col] })))
    .map(({ cx, cy, fill }) => `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${fill}"/>`)
    .join("\n    ");
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="${rx}" fill="${INK}"/>
    ${dots}
</svg>
`;
}

const tmp = mkdtempSync(path.join(tmpdir(), "popsim-icons-"));
const render = (name, source, size) => {
  const svgPath = path.join(tmp, `${name}.svg`);
  const pngPath = path.join(tmp, `${name}-${size}.png`);
  writeFileSync(svgPath, source);
  execFileSync("inkscape", [svgPath, "--export-type=png", `--export-filename=${pngPath}`, "-w", String(size), "-h", String(size)], { stdio: "pipe" });
  return pngPath;
};

// Tab icon: rounded-square SVG served directly.
writeFileSync(path.join(root, "site", "favicon.svg"), svg({ rx: 96, inset: 0 }));

// Legacy .ico from the same art at 48/32/16.
const icoSources = [48, 32, 16].map((size) => render("favicon", svg({ rx: 96, inset: 0 }), size));
execFileSync("convert", [...icoSources, path.join(root, "site", "favicon.ico")], { stdio: "pipe" });

// Apple touch icon: full-bleed square, grid pulled in for iOS's own mask.
mkdirSync(path.join(root, "site", "icons"), { recursive: true });
execFileSync("convert", [render("apple", svg({ rx: 0, inset: 0.12 }), 180), path.join(root, "site", "icons", "apple-touch-icon.png")], { stdio: "pipe" });

rmSync(tmp, { recursive: true, force: true });
console.log("wrote site/favicon.svg, site/favicon.ico, site/icons/apple-touch-icon.png");
