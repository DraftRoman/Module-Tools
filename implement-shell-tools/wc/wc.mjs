import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program
  .name("wc")
  .description("A program to implement word, character and line counter.")
  .option("-l", "Counts the lines in a file")
  .option("-w", "Counts the words in a file")
  .option("-c", "Counts the characters in a file")
  .argument("<filepath...>");

program.parse(process.argv);

const opts = program.opts();
const args = program.args;

if (args.length === 0) {
  console.error(`Expected at least one argument but received ${args.length}`);
  process.exit(1);
}

let totalLines = 0;
let totalWords = 0;
let totalChars = 0;

for (const file of args) {
  const content = await fs.readFile(file, "utf-8");
  const linesArr = content.split('\n');
  const lines = linesArr[linesArr.length - 1] === '' ? linesArr.length - 1 : linesArr.length;
  const words = content.split(/\s+/).filter(Boolean).length;
  const chars = content.length;
    
  totalLines += lines;
  totalWords += words;
  totalChars += chars;

  let output = '';
  if (opts.l) output += `${lines} `;
  if (opts.w) output += `${words} `;
  if (opts.c) output += `${chars} `;
  if (!opts.l && !opts.w && !opts.c) output += `${lines} ${words} ${chars} `;
  output += file;
  console.log(output);
}

if (args.length > 1) {
  let totalOutput = '';
  if (opts.l) totalOutput += `${totalLines} `;
  if (opts.w) totalOutput += `${totalWords} `;
  if (opts.c) totalOutput += `${totalChars} `;
  if (!opts.l && !opts.w && !opts.c) totalOutput += `${totalLines} ${totalWords} ${totalChars} `;
  totalOutput += 'total';
  console.log(totalOutput);
}