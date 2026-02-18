import { program } from "commander";
import { promises as fs } from "node:fs";

program
  .name("ls")
  .description("Displays files in a directory")
  .option("-1, --one", "Display each file on a new line")// for listing one file per line
  .option("-a, --all", "Include hidden files")
  .argument("[filepath]", "Directory to list files from (default: current)")

await program.parseAsync();  

const opts = program.opts();
const args = program.args;

const path = args[0] || "."; //Use current directory if no path provided
let files ;
try {
    files = await fs.readdir(path);
}catch (err) {
    console.error(`ls: cannot access '${path}': ${err.message}`);
    process.exit(1);

}

if (!opts.all) {
  files = files.filter(file => !file.startsWith("."));// if path not provided use current directory
}

if (opts.one) {
  files.forEach(file => console.log(file));
} else {
  console.log(files.join(" "));
}

