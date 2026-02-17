import { program } from "commander";
import { promises as fs } from "node:fs";

program
  .name("myCat")
  .description("Simple file viewer")
  .option("-n", "Number all output lines")
  .option("-b", "Number non-blank output lines")
  .argument("<path...>", "One or more file paths to show");

program.parse();

const files = program.args;
const opts = program.opts();
let lineNumber = 1;

for (const filename of files) {
  const content = await fs.readFile(filename, "utf-8");
  const lines = content.split("\n");

  if (opts.n) {

    for (const line of lines) {
      console.log(lineNumber + " " + line);
      lineNumber++;
    }
  } else if (opts.b) {

    for (const line of lines) {
      if (line.trim() !== "") {
        console.log(lineNumber + " " + line);
        lineNumber++;
      }
    }
  } else {
    console.log(content);
  }
}
