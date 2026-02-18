import { program } from "commander";
import process from "node:process";
import { promises as fs } from "node:fs";
import glob from "glob";

program
  .name("cat")
  .description("print the content of file")
  .option("-n, --line-numbers", "Number the output lines, starting at 1")
  .option(
    "-b, --number-nonblank",
    "Number non-empty output lines, overrides -n"
  )
  .argument("<paths...>", "The file path(s) to process"); // to support multiple file
program.parse();

const argv = program.args.flatMap((path) => glob.sync(path));

const options = program.opts();
if (argv.length === 0) {
  console.error(`No file paths provided`); // to support more files
  process.exit(1);
}

let lineCounter = 1;
function printLine(line, number = false) {
  if (number && line.trim() !== "") {
    const lineNumber = String(lineCounter++).padStart(6, " ");
    console.log(`${lineNumber}\t${line}`);
  } else {
    console.log(line);
  }
}
// Helper function to print totals for multiple files
function printTotal(total, label = "total") {
  console.log(`${total} ${label}`);
}
for (const path of argv) {
  try {
    const content = await fs.readFile(path, "utf-8");
    const lines = content.split(/\r?\n/);
    if (lines.length && lines[lines.length - 1] === "") {
      // Remove trailing empty line if it's just from the final newline
      lines.pop();
    }
    // Determine if we need to number lines
    const numberLines = options.numberNonblank || options.lineNumbers;

    lines.forEach((line) => printLine(line, numberLines));

    // Add a newline if the file didn't end with one
    if (!content.endsWith("\n")) process.stdout.write("\n");
  } catch (err) {
    console.error(`cat: ${path}: ${err.message}`);
  }
}
