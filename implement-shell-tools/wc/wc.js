#!/usr/bin/env node

const fs = require("fs");
const path = require("path");

// -------- argument parsing --------
const args = process.argv.slice(2);

let countLines = false;
let countWords = false;
let countBytes = false;
let files = [];

// flags can appear in any order
for (const arg of args) {
  if (arg === "-l") countLines = true;
  else if (arg === "-w") countWords = true;
  else if (arg === "-c") countBytes = true;
  else files.push(arg);
}

if (files.length === 0) {
  console.error("Usage: wc [-l] [-w] [-c] <file> [file...]");
  process.exit(1);
}

// If no flags → behave like plain `wc`
if (!countLines && !countWords && !countBytes) {
  countLines = true;
  countWords = true;
  countBytes = true;
}

// -------- helpers --------
function countFile(filePath) {
  let content;
  let buffer;

  try {
    buffer = fs.readFileSync(filePath);
    content = buffer.toString("utf8");
  } catch (err) {
    console.error(`wc.js: ${filePath}: ${err.message}`);
    return null;
  }

  const lines = content.split("\n").length - 1;
  const words = content.trim() === ""
    ? 0
    : content.trim().split(/\s+/).length;
  const bytes = buffer.length;

  return { lines, words, bytes };
}

function formatOutput(counts, fileName) {
  const parts = [];

  if (countLines) parts.push(counts.lines.toString().padStart(7, " "));
  if (countWords) parts.push(counts.words.toString().padStart(7, " "));
  if (countBytes) parts.push(counts.bytes.toString().padStart(7, " "));

  parts.push(" " + fileName);
  return parts.join("");
}

// -------- main --------
let total = { lines: 0, words: 0, bytes: 0 };
let validFileCount = 0;

for (const file of files) {
  const counts = countFile(file);
  if (!counts) continue;

  validFileCount++;

  total.lines += counts.lines;
  total.words += counts.words;
  total.bytes += counts.bytes;

  process.stdout.write(formatOutput(counts, file) + "\n");
}

// Print total if multiple files
if (validFileCount > 1) {
  process.stdout.write(formatOutput(total, "total") + "\n");
}
