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


const folderPath = program.args[0] || "./";
const files = await fs.readdir(folderPath);
const coloredFiles = [];

for (const file of files) {
    const fullPath = `${folderPath}/${file}`;
    const stats = await fs.stat(fullPath, (err, stats) => {
        if (err)
            console.error(err);
        exit(1);
        return stats;
    });
    if (stats.isDirectory()) {
        coloredFiles.push(chalk.blue(file));
    } else {
        coloredFiles.push(file);
    }
}

console.log(coloredFiles.join(" "));
