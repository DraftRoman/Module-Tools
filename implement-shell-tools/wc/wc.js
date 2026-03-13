import { program } from "commander";
import { promises as fs } from "node:fs";

program
  .name("wc command")
  .description("Implement wc command to count words and lines")
  .option("-l, --lines", "show number of lines only")
  .option("-w, --words", "show number of words only")
  .option("-c, --chars", "show number of characters only")
  .argument("[paths...]", "The file path to process");

program.parse(process.argv);

const opts = program.opts();
let paths = program.args;

if (paths.length === 0) {
  paths = ["."];
}

let totals = { lines: 0, words: 0, chars: 0 };

for (const filePath of paths) {
  let content;
  try {
    content = await fs.readFile(filePath, "utf8");
  } catch (err) {
    console.error(`wc: cannot read file "${filePath}": ${err.message}`);
    continue; 
  }

  const lineCount = content.split("\n").length;
  const wordCount = content.split(/\s+/).filter(Boolean).length;
  const charCount = content.length;

  totals.lines += lineCount;
  totals.words += wordCount;
  totals.chars += charCount;

  const output = [];

  if (!opts.lines && !opts.words && !opts.chars) {
    output.push(lineCount, wordCount, charCount);
  } else {
    if (opts.lines) output.push(lineCount);
    if (opts.words) output.push(wordCount);
    if (opts.chars) output.push(charCount);
  }
  console.log(`${output.join(" ")} ${filePath}`);
}

if (paths.length > 1) {
  const totalOutput = [];

  if (!opts.lines && !opts.words && !opts.chars) {
    totalOutput.push(totals.lines, totals.words, totals.chars);
  } else {
    if (opts.lines) totalOutput.push(totals.lines);
    if (opts.words) totalOutput.push(totals.words);
    if (opts.chars) totalOutput.push(totals.chars);
  }
  console.log(`${totalOutput.join(" ")} total`);
}
