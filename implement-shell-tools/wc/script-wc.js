#!/usr/bin/env node
import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

// Setup CLI
program
  .name("wc-clone")
  .description("A simplified implementation of the wc command")
  .option("-l", "count lines")
  .option("-w", "count words")
  .option("-c", "count bytes")
  .argument("[files...]", "files to process");

program.parse();

const options = program.opts();
const files = program.args;

if (files.length === 0) {
  console.error("Please provide at least one file.");
  process.exit(1);
}

// Count lines, words, bytes
function countContent(content) {
  const lines = content.split("\n").length;
  const words = content.trim().split(/\s+/).filter(Boolean).length;
  const bytes = Buffer.byteLength(content, "utf-8");
  return { lines, words, bytes };
}

// Format output consistently
function formatOutput(counts, label = "") {
  const showAll = !options.l && !options.w && !options.c;
  const parts = [];

  if (options.l || showAll) parts.push(counts.lines.toString().padStart(8));
  if (options.w || showAll) parts.push(counts.words.toString().padStart(8));
  if (options.c || showAll) parts.push(counts.bytes.toString().padStart(8));

  if (label) parts.push(label);

  return parts.join(" ");
}

(async () => {
  let total = { lines: 0, words: 0, bytes: 0 };
  const multipleFiles = files.length > 1;

  for (const file of files) {
    let content;
    try {
      content = await fs.readFile(file, "utf-8");
    } catch {
      console.error(`wc-clone: cannot open '${file}': No such file`);
      continue;
    }

    const counts = countContent(content);

    total.lines += counts.lines;
    total.words += counts.words;
    total.bytes += counts.bytes;

    console.log(formatOutput(counts, file));
  }

  if (multipleFiles) {
    console.log(formatOutput(total, "total"));
  }
})();
