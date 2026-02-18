import {program} from "commander";
import {promises as fs} from "node:fs";

program
.name("ls")
.description("displays files in a directory")
.option("-1, --one", "displays each file in its own line")
.option("-a, --all", "displays all files including hidden files")
.arguments("<filepath>")

await program.parseAsync();

const opts = program.opts();
const args = program.args;

if (args.length === 0) {
  console.error("Error: Missing <filepath> argument.");
  program.help();
}

const path = args[0];
const files = await fs.readdir(path);

let visibleFiles = files;
if (!opts.all) {
  visibleFiles = files.filter(file => !file.startsWith("."));
}

if (opts.one) {
  visibleFiles.forEach(console.log);
} else {
  console.log(visibleFiles.join(" "));
}