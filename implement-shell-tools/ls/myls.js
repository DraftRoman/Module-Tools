import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program
  .name("myls")
  .description("list file(s) in the directory, like the ls command")
  .option("-1", "list one file per line")
  .option("-a", "include hidden files")
  .argument("[directory]", "Directory to list", ".");

program.parse();

const options = program.opts();
const directory = program.args[0] || ".";

try {
  let files = await fs.readdir(directory);

  // if "-a" is used, include hidden files; those that start with "."
  if (options.a) {
    files = [".", "..", ...files];
  }

  // If "-a" is not used, filter hidden files out
  files = files.filter((file) => options.a || !file.startsWith("."));

  // Sort alphabetically
  files.sort();

  if (options["1"]) {
    // Print one file per line
    for (const file of files) {
      console.log(file);
    }
  } else {
    // Print all files on a single line, separated by spaces
    console.log(files.join(" "));
  }
} catch (error) {
  console.error(`Error reading directory ${directory}:`, error.message);
  process.exit(1);
}