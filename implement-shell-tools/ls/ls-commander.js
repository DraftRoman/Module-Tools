import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program 
    .name("list-files")
    .description("List files in a directory")
    .option("-1", "Show line by line")
    .option("-a, --all", "Show hidden files")
    .argument("[paths...]", "The directory paths",["."]);

program.parse();

const argv = program.args;

if (argv.length != 1){
    console.error(`Expected exactly 1 argument (a path) to be passed but got ${argv.length}`);
    process.exit(1);
}
const dirPath = argv[0];
const options = program.opts();

const entries = await fs.readdir(dirPath)

const listFiles = entries.map((entry) => `${entry.padStart(6)}` )
const noHidden = listFiles.filter(name => !name.startsWith('.'));

if (options.all && options[1]){
    console.log(listFiles.join('\n'));
} else if (options.all) {
    console.log(listFiles.join(' '));
} else if (options[1]){
    console.log(noHidden.join('\n'));
} else {
    console.log(noHidden.join(' '));
}
