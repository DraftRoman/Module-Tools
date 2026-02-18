import { program } from "commander";
import{promises as fs} from "node:fs";


program
.name("cat")
.description("displays the contents of a file")
.option("-n, --number", "Number all output lines")
.option("-b, --number-nonblank", "Number non-blank output lines only")
.argument("<filepaths...>");

program.parse();


const args = program.args;
const opts = program.opts();

if (args.length === 0) {
  console.error("Error: Missing <filepath> argument.");
  program.help();
}

let globalLineNumber = 1;

for (const path of args) {
  try {
    const content = await fs.readFile(path, "utf-8");
    const lines = content.split('\n');

    if (opts.number) {
      lines.forEach((line, idx) => {
        console.log(`${idx + 1}\t${line}`);
      });
    } else if (opts.numberNonblank) {
      for (const line of lines) {
        if (line.trim() !== '') {
          console.log(`${globalLineNumber}\t${line}`);
          globalLineNumber++;
        }
      }
    } else {
      console.log(content);
    }
  } catch (err) {
    console.error(`Error reading file "${path}": ${err.message}`);
  }
}