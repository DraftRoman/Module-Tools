import {program} from "commander";
import{promises as fs} from "node:fs";

program
.name("wc")
.description("counts lines, words, and bytes")
.option("-l, --line", "counts number of lines in the file")
.option("-w, --words", "counts number of words in the file")
.option("-c, --bytes", "counts number  of bytes in the file")
.argument("<filepaths...>")

program.parse();

const args= program.args;
const opts = program.opts();

if(args.length === 0){
    console.error("Error: Missing <filepath> argument.");
  program.help();
}

const countLines = content => content.split(/\r?\n/).length;
const countWords = content => content.trim().split(/\s+/).filter(Boolean).length;
const countBytes = content => Buffer.byteLength(content, "utf-8");

// store totals for multiple files
let totalLines = 0;
let totalWords = 0;
let totalBytes = 0;

for (const path of args) {
  try {
    const content = await fs.readFile(path, "utf-8");

    const lines = countLines(content);
    const words = countWords(content);
    const bytes = countBytes(content);

    totalLines += lines;
    totalWords += words;
    totalBytes += bytes;

    // collect counts based on options
    const output = [];
    if (opts.line) output.push(lines);
    if (opts.words) output.push(words);
    if (opts.bytes) output.push(bytes);

    // if no options are passed, print all
    if (!opts.line && !opts.words && !opts.bytes) {
      output.push(lines, words, bytes);
    }

    console.log(...output, path);
  } catch (err) {
    console.error(`Error reading file "${path}": ${err.message}`);
  }
}

// print totals if more than one file
if (args.length > 1) {
  const totalOutput = [];
  if (opts.line) totalOutput.push(totalLines);
  if (opts.words) totalOutput.push(totalWords);
  if (opts.bytes) totalOutput.push(totalBytes);

  if (!opts.line && !opts.words && !opts.bytes) {
    totalOutput.push(totalLines, totalWords, totalBytes);
  }

  console.log(...totalOutput, "total");
}