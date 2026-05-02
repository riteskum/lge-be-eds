#!/usr/bin/env node
/**
 * Fetch Figma node 1-668 (PDP) — text tree + image refs.
 * Do NOT commit tokens. Use env or pass token once locally.
 *
 * Usage:
 *   set FIGMA_TOKEN=figd_...   (Windows: set FIGMA_TOKEN=figd_...)
 *   node scripts/fetch-figma-pdp.mjs
 *
 * Or:
 *   node scripts/fetch-figma-pdp.mjs figd_YOUR_TOKEN
 *
 * On 429: wait 15–60 minutes and retry (Figma rate limits per token).
 */

const FILE_KEY = 'ejyEiI2q4cMTZBFGymUaLA';
const NODE_ID = '1-668'; // URL node-id=1-668

const token = process.argv[2] || process.env.FIGMA_TOKEN;
if (!token) {
  console.error('Set FIGMA_TOKEN or pass token as first argument.');
  process.exit(1);
}

function walk(node, depth = 0) {
  const pad = '  '.repeat(depth);
  const name = node.name || '?';
  const type = node.type || '?';
  let line = `${pad}${type}: ${name}`;
  if (node.characters) {
    line += ` => "${String(node.characters).slice(0, 200).replace(/\s+/g, ' ')}"`;
  }
  const fills = node.fills || [];
  for (const f of fills) {
    if (f.type === 'IMAGE' && f.imageRef) {
      line += ` [imageRef: ${f.imageRef}]`;
    }
  }
  console.log(line);
  for (const c of node.children || []) {
    walk(c, depth + 1);
  }
}

const url = `https://api.figma.com/v1/files/${FILE_KEY}/nodes?ids=${encodeURIComponent(NODE_ID)}&depth=15`;
const res = await fetch(url, { headers: { 'X-Figma-Token': token } });
const data = await res.json();

if (!res.ok || data.err) {
  console.error('Figma API error:', data.status || res.status, data.err || data);
  process.exit(1);
}

const doc = data.nodes?.['1:668']?.document;
if (!doc) {
  console.error('Node 1:668 not found. Keys:', Object.keys(data.nodes || {}));
  process.exit(1);
}

console.log('\n--- PDP frame (1-668) text / images ---\n');
walk(doc);

await import('node:fs').then((fs) => {
  fs.writeFileSync(
    new URL('../fig_pdp_dump.json', import.meta.url),
    JSON.stringify(data, null, 2),
  );
  console.log('\nWrote fig_pdp_dump.json (gitignored pattern fig_*.json)\n');
});
