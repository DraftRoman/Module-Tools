import { promises as fs } from "node:fs";
import { program } from "commander";
import chalk from "chalk";

program
    .name("myLs")
    .description("The re-implementation of the ls command")
    .argument("[path]", "path to the directory", "./")
    .option("-1, --column", "file in one line")
    .option("-a, --all", "show all files")
  
program.parse();

const options = program.opts();
const folderPath = program.args[0] || "./";
const dotsArray = [".", ".."];
const files = await fs.readdir(folderPath);
let visibleFiles = options.all ? dotsArray.concat(files) : files.filter(file => !file.startsWith("."));
const coloredFiles = [];

for (const file of visibleFiles) {
    const fullPath = `${folderPath}/${file}`;
    const stats = await fs.stat(fullPath, (err, stats) => {
        if (err)
            console.error(err);
        exit(1);
        return stats;
    });
    if (stats.isDirectory()) {
        coloredFiles.push(chalk.blue(file));
    } else if (file.startsWith("."))
{
        coloredFiles.push(chalk.yellow(file));
    } else {
        coloredFiles.push(file);
    }
}

if (options.column) {
    for (const file of coloredFiles) {
        console.log(file);
    }
}
else {
    console.log(coloredFiles.join(" "));
}
