#!/usr/bin/env node

const fs = require("fs");
const path = require("path");

// -------- args parsing --------
const args = process.argv.slice(2);

let onePerLine = false; // -1
let showAll = false;    // -a
let targets = [];

for (const arg of args) {
  if (arg === "-1") onePerLine = true;
  else if (arg === "-a") showAll = true;
  else targets.push(arg);
}

// Coursework only tests -1 variants, so enforce it clearly
if (!onePerLine) {
  console.error("Usage: node ls.js -1 [-a] [path]");
  process.exit(1);
}

if (targets.length === 0) targets = ["."];
if (targets.length > 1) {
  console.error("ls.js: only one path is supported in this exercise");
  process.exit(1);
}

const target = targets[0];

// -------- helpers --------
function sortLikeLs(names) {
  return names.sort((a, b) => a.localeCompare(b));
}

function listDir(dirPath) {
  let entries;
  try {
    entries = fs.readdirSync(dirPath, { withFileTypes: false });
  } catch (err) {
    console.error(`ls.js: cannot access '${dirPath}': ${err.message}`);
    process.exit(1);
  }

  // readdirSync does NOT include "." and ".." — ls -a does.
  if (showAll) {
    // keep dotfiles + add . and ..
    entries = [".", "..", ...entries];
  } else {
    // hide dotfiles
    entries = entries.filter((name) => !name.startsWith("."));
  }

  entries = sortLikeLs(entries);

  // -1 => one per line
  for (const name of entries) {
    process.stdout.write(name + "\n");
  }
}

function listFile(filePath) {
  // ls -1 file => prints the file name
  process.stdout.write(path.basename(filePath) + "\n");
}

// -------- main --------
let stat;
try {
  stat = fs.statSync(target);
} catch (err) {
  console.error(`ls.js: cannot access '${target}': ${err.message}`);
  process.exit(1);
}

if (stat.isDirectory()) listDir(target);
else listFile(target);
