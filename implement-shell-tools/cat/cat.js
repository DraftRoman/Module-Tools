import { promises as fs } from "node:fs";
import { program } from "commander";

program
  .name("myCat")
  .description("The re-implementation of the cat command")
  .argument("<file>", "file to read")
  .option("-n, --number", "number all lines")
  .option("-b, --number-nonblank", "number non-empty lines");

program.parse();

const options = program.opts();
const path = program.args[0];

try {
    let content = await fs.readFile(path, "utf-8");
    const lines = content.split("\n");
    if (options.numberNonblank) {
    let lineNumber = 1;
        content = lines.map(line => {
            if (line.trim() === "") return line;
            return `${lineNumber++} ${line}`;
        }).join("\n");
    } else if (options.number) {
        content = lines.map((line, index) => `${index + 1} ${line}`).join("\n");
    }
    
    console.log(content);
} catch (err) {
    console.error(`Error reading file: ${err.message}`);
    process.exit(1);
}
