import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program
  .name("display-file-content")
  .description("Implement cat command with -n and -b flag support")
  .option("-n, --number-all-lines", "Number every line in the file")
  .option("-b, --number-non-empty-lines", "Number non empty lines in the file")
  .argument("<paths...>", "File paths to process");

program.parse(process.argv);

const filepaths = program.args;

const options = program.opts();

let lineNumber = 1;

for (const filepath of filepaths) {
  const fileContent = await fs.readFile(filepath, "utf8");
  const lines = fileContent.split("\n");

  for (const line of lines) {
    if (options.numberAllLines) {
      console.log(`${lineNumber} ${line}`);
      lineNumber++;
      continue;
    }

    if (options.numberNonEmptyLines) {
      if (line.trim() === "") {
        console.log(line);
      } else {
        console.log(`${lineNumber} ${line}`);
        lineNumber++;
      }
      continue;
    }
    console.log(line);
  }
}
