import { program } from "commander";
import { promises as fs } from "node:fs";

program
  .name("node-ls")
  .description("A Node.js implementation of the Unix ls command")
  .option("-1", "list one file per line")
  .option(
    "-a, --all",
    "include directory entries whose names begin with a dot (.)"
  )
  .argument("[directory]", "The file path to process");
program.parse();

const { 1: onePerLine, all } = program.opts();
const directory = program.args[0] ? program.args[0] : ".";

let entries = await fs.readdir(directory);

// If -a is used, I've included  "." and ".." to mimic what the Unix ls does
if (all) {
  entries = [".", "..", ...entries];
} else {
  // hide dotfiles
  entries = entries.filter((entry) => entry[0] !== ".");
}

if (onePerLine) {
  console.log(entries.join("\n"));
} else {
  console.log(entries.join("  "));
}
