import { program } from "commander";
import { promises as fs } from "node:fs";

program
  .name("node-cat")
  .description("A Node.js implementation of the Unix cat command")
  .option("-n, --number", "Number all output lines")
  .option(
    "-b, --numberNonBlank",
    "Numbers only non-empty lines. Overrides -n option"
  )
  .argument("<path...>", "The file path to process");

program.parse();

const paths = program.args;
const { number, numberNonBlank } = program.opts();

// --- Read files ---
let content = "";

for (const path of paths) {
  content += await fs.readFile(path, "utf-8");
}

// Remove the trailing newline
// I do realise that this is not exactly how cat works, but for the files that we have, we get a trailing new line and this makes the output look just as it would with the Unix cat command.
if (content.endsWith("\n")) {
  content = content.slice(0, -1);
}

const contentLines = content.split("\n");

// --- Numbering functions ---
function numberAll(lines) {
  return lines.map(
    (line, index) => `${String(index + 1).padStart(6, " ")}  ${line}`
  );
}

function numberNonEmpty(lines) {
  let lineCounter = 1;
  return lines.map((line) =>
    line.trim() === ""
      ? line
      : `${String(lineCounter++).padStart(6, " ")}  ${line}`
  );
}

// --- Output logic ---
let output;

if (numberNonBlank) {
  output = numberNonEmpty(contentLines);
} else if (number) {
  output = numberAll(contentLines);
} else {
  output = contentLines;
}

// --- Print output ---
console.log(output.join("\n"));
