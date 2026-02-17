import { program } from "commander";
import { promises as fs } from "node:fs";

program
  .name("myLs")
  .description("my ls clone")
  .option("-1, --one-per-line", "one entry per line")
  .option("-a", "show hidden files")
  .argument("[paths...]", "file or directory paths");

program.parse();

const opts = program.opts();
let paths = program.args;

if (paths.length === 0) {
  paths = ["."];
}

for (const path of paths) {
  const directoryItems = await fs.readdir(path);

  for (const file of directoryItems) {
    if (!opts.a && file.startsWith(".")) {
      continue;
    }

    if (opts.onePerLine) {
      console.log(file);
    } else {
      console.log(file + " ");
    }
  }

}
