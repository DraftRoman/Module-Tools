import { program } from "commander";
import process from "node:process";
import { promises as fs } from "node:fs";

program
  .name("cat")
  .description("Prints file contents to the terminal")
  .option("-n", "number all output lines")
  .argument("<files...>", "Files to print");

program.parse();

const opts = program.opts();
const files = program.args;

if (files.length < 1) {
  console.error("Please specify one or more files.");
  process.exit(1);
}

async function printFileContent(filename) {
  try {
    const content = await fs.readFile(filename, "utf-8");
    if (opts.n) {
      const lines = content.split("\n");
      for (let i = 0; i < lines.length; i++) {
        console.log(`${(i + 1).toString().padStart(6, " ")}\t${lines[i]}`);
      }
    } else {
      process.stdout.write(content);
    }
  } catch {
    console.error(`Could not read file: ${filename}`);
  }
}

(async () => {
  for (const file of files) {
    await printFileContent(file);
  }
})();
