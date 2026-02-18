import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";


program
  .name("Display the contents of a file")
  .description("Should effectively display the contents of a file as cat does even with extra flags")
  .option("-n", "The character numbers all the lines of output.")
  .option("-b", "The character numbers only the nonempty lines of the output")
  .argument("<files...>");

program.parse();

const files = program.args;
const options = program.opts();

if (files.length === 0) {
  console.error(`Expected at least 1 argument (a path) to be passed but got ${files.length}.`);
  process.exit(1);
}

let lineNum = 1;

for (const file of files) {
  const content = await fs.readFile(file, "utf-8");
  const lines = content.split("\n");

  for (const line of lines) {
    if (options.b) {
      if (line.trim() !== "") {
        console.log(`${(lineNum).toString().padStart(6)}  ${line}`);
        lineNum++;
      }
      else {
        console.log(line);
      }
    }
    else if (options.n) {
      console.log(`${(lineNum).toString().padStart(6)}  ${line}`);
      lineNum++;
    }
    else {
      console.log(line);
    }
  }

}
