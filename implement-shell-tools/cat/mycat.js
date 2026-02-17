import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program
  .name("mycat")
  .description("Outputs the content of the given file(s), like the cat command")
  .option("-n", "Number all lines")
  .option("-b", "Number non-blank lines only")
  .argument("<files...>", "File paths to display");

program.parse();

const options = program.opts();
const filePaths = program.args;

let lineNumber = 1;

for (const path of filePaths) {
  try {
    const content = await fs.readFile(path, "utf-8");
    const lines = content.trimEnd().split("\n");

    for (const line of lines) {
      const isBlank = line.trim() === "";

      if (options.b) {
        // -b: number only non-blank lines
        if (!isBlank) {
          process.stdout.write(`${String(lineNumber).padStart(6)}  ${line}\n`);
          lineNumber++;
        } else {
          process.stdout.write("\n");
        }
      } else if (options.n) {
        // -n: number all lines
        process.stdout.write(`${String(lineNumber).padStart(6)}  ${line}\n`);
        lineNumber++;
      } else {
        // no flags
        process.stdout.write(line + "\n");
      }
    }
  } catch (error) {
    process.stderr.write(`Error reading file ${path}: ${error.message}\n`);
    process.exit(1);
  }
}
