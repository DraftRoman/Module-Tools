import { program } from "commander";
import { promises as fs } from "node:fs";
import pkg from "glob";
const { glob } = pkg;

program
  .name("wc")
  .description("Count lines, words, and bytes in files")
  .option("-l, --lines", "Only print line counts")
  .option("-w, --words", "Only print word counts")
  .option("-c, --bytes", "Only print byte counts")
  .argument("<files...>", "One or more files to process");
await program.parseAsync();

const files = program.args.flatMap((path) => glob.sync(path));
const options = program.opts();

function countContent(content) {
  const lines = (content.match(/\n/g) || []).length;
  const words = content.trim().split(/\s+/).filter(Boolean).length;
  const bytes = Buffer.byteLength(content, "utf-8");
  return { lines, words, bytes };
}
// Helper to print counts based on options
function printCounts({ lines, words, bytes }, label) {
  if (options.lines) {
    console.log(`${lines} ${label}`);
  } else if (options.words) {
    console.log(`${words} ${label}`);
  } else if (options.bytes) {
    console.log(`${bytes} ${label}`);
  } else {
    console.log(`${lines} ${words} ${bytes} ${label}`);
  }
}

let totalLines = 0;
let totalWords = 0;
let totalBytes = 0;

for (const file of files) {
  try {
    const content = await fs.readFile(file, "utf-8");
    const counts = countContent(content);

    printCounts(counts, file);

    totalLines += counts.lines;
    totalWords += counts.words;
    totalBytes += counts.bytes;
  } catch (err) {
    console.error(`wc: ${file}: ${err.message}`);
  }
}

if (files.length > 1) {
  printCounts(
    { lines: totalLines, words: totalWords, bytes: totalBytes },
    "total"
  );
}
