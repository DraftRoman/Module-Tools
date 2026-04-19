import { promises as fs } from "node:fs";
import { program } from "commander";

program
  .name("myWordCounter")
  .description("The re-implementation of the wc command")
  .argument("<files...>", "files to read")
  .option("-l, --lines", "count lines")
  .option("-w, --words", "count words")
  .option("-c, --symbols", "count symbols");

program.parse();

const options = program.opts();
const paths = program.args;

  for (const path of paths) {
    try {
      const content = await fs.readFile(path, "utf-8");

      let lineCount = (content.match(/\n/g)).length;
      let wordCount = content.trim() ? content.trim().split(/\s+/).length : 0;
      let symbolCount = content.length;

      if (options.lines || options.words || options.symbols) {
        let output = "";
        if (options.lines) output += `${lineCount} `;
        if (options.words) output += `${wordCount} `;
        if (options.symbols) output += `${symbolCount} `;
        console.log(`${output}${path}`);
      } 
      else {
        console.log(`${lineCount} ${wordCount} ${symbolCount} ${path}`);
      }
    } catch (err) {
      console.error(`Error reading file ${path}: ${err.message}`);
    }
  }


