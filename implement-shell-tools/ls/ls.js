import { program } from "commander";
import { promises as fs } from "node:fs";

program
  .name("list-files-in-directory")
  .description("Implement ls command to list files in directory")
  .option("-1, --one-per-line", "list files one per line")
  .option("-a, --allFiles", "list all files including hidden ones")
  .argument("[paths...]", "File paths to process");

program.parse(process.argv);

const options = program.opts();

let paths = program.args;
if (paths.length === 0) paths = ["."];

for (const directoryPath of paths) {
  let fileNames;

  try {
    fileNames = await fs.readdir(directoryPath);
  } catch (err) {
    console.error(`ls: cannot access '${directoryPath}': ${err.message}`);
    continue;
  }

  fileNames = fileNames.filter(
    (file) => options.allFiles || !file.startsWith("."),
  );

  if (options.onePerLine) {
    for (const file of fileNames) {
      console.log(file);
    }
  } else {
    console.log(fileNames.join(" "));
  }
}
