import { program } from "commander";
import process from "node:process";
import { promises as fs } from "node:fs";

program
    .name("ls")
    .description("Lists files in a directory like ls -1")
    .option("-1", "List one file per line") 
    .option("-a", "Show hidden files also") 
    .argument("[dir]", "The directory to list (optional, default: current)");

program.parse();


const argv = program.args;
const dir = argv[0] || "."; 


if (argv.length > 1) {
    console.error(`Expected at most 1 argument (directory) but got ${argv.length}.`);
    process.exit(1);
}

try {
    const files = await fs.readdir(dir);
    const showHidden = program.opts().a;
    const filtered = showHidden ? files : files.filter(f => !f.startsWith("."));
    for (const f of filtered) {
        console.log(f);
    }
} catch {
    console.error(`Could not read directory: ${dir}`);
    process.exit(1);
}