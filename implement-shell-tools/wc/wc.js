import { program } from "commander";
import { promises as fs } from "node:fs";
import { stat } from "node:fs/promises";

program
  .name("my-wc")
  .description("Simplified implementation of wc")
  .argument("[paths...]", "One or more file or directory paths")
  .option("-l, --line", "Count lines")
  .option("-w, --word", "Count words")
  .option("-c, --character", "Count characters");

program.parse();

const filePaths = program.args.length > 0 ? program.args : ['.'];
const options = program.opts();

const countContent = (content) => {
  const lines = content.split('\n').length;
  const words = content.trim().split(/\s+/).filter(Boolean).length;
  const characters = content.length;
  return { lines, words, characters };
};

const total = {
  lines: 0,
  words: 0,
  characters: 0
};

//Output formatting function
function formatOutput(counts, label, options) {
  const { lines, words, characters } = counts;
  const showAll = !options.line && !options.word && !options.character;

  const parts = [];

  if (options.line || showAll) parts.push(lines.toString().padStart(8));
  if (options.word || showAll) parts.push(words.toString().padStart(8));
  if (options.character || showAll) parts.push(characters.toString().padStart(8));

  parts.push(label);
  return parts.join(" ");
}

(async () => {
  let fileCount = 0;

  for (const inputPath of filePaths) {
    try {
      const stats = await stat(inputPath);
      if (stats.isDirectory()) {
        console.log(`${inputPath} is a directory. Skipping.`);
        continue;
      }

      const content = await fs.readFile(inputPath, "utf-8");
      const counts = countContent(content);

      total.lines += counts.lines;
      total.words += counts.words;
      total.characters += counts.characters;
      fileCount++;

      console.log(formatOutput(counts, inputPath, options));
    } catch (err) {
      console.error(`Error reading "${inputPath}": ${err.message}`);
    }
  }

  if (fileCount > 1) {
    console.log(formatOutput(total, "total", options));
  }
})();
