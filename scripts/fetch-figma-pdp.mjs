#!/usr/bin/env node
/**
 * Fetch Figma node 1-668 (PDP) — text tree + image refs.
 * Do NOT commit tokens. Use `.env`, env var, or pass token once locally.
 *
 * Usage:
 *   1. Copy `.env.example` to `.env` and set FIGMA_TOKEN=figd_...
 *   2. node scripts/fetch-figma-pdp.mjs
 *
 * Or:
 *   set FIGMA_TOKEN=figd_...
 *   node scripts/fetch-figma-pdp.mjs
 *
 * Or:
 *   node scripts/fetch-figma-pdp.mjs figd_YOUR_TOKEN
 *
 * On 429: wait 15–60 minutes and retry (Figma rate limits per token).
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.join(__dirname, '..');

function loadDotEnv() {
  const envPath = path.join(repoRoot, '.env');
  if (!fs.existsSync(envPath)) return;
  const text = fs.readFileSync(envPath, 'utf8');
  for (const line of text.split('\n')) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) continue;
    const eq = trimmed.indexOf('=');
    if (eq === -1) continue;
    const key = trimmed.slice(0, eq).trim();
    let val = trimmed.slice(eq + 1).trim();
    if ((val.startsWith('"') && val.endsWith('"')) || (val.startsWith("'") && val.endsWith("'"))) {
      val = val.slice(1, -1);
    }
    if (key === 'FIGMA_TOKEN' && val && !process.env.FIGMA_TOKEN) {
      process.env.FIGMA_TOKEN = val;
    }
  }
}

loadDotEnv();

const FILE_KEY = 'ejyEiI2q4cMTZBFGymUaLA';
const NODE_ID = '1-668'; // URL node-id=1-668

const token = process.argv[2] || process.env.FIGMA_TOKEN;
if (!token) {
  console.error('Missing token: add FIGMA_TOKEN to `.env` (see `.env.example`), or pass as first argument.');
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

fs.writeFileSync(
  path.join(repoRoot, 'fig_pdp_dump.json'),
  JSON.stringify(data, null, 2),
);
console.log('\nWrote fig_pdp_dump.json (gitignored pattern fig_*.json)\n');
