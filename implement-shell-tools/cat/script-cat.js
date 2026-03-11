#!/usr/bin/env node
import { program } from "commander";
import { promises as fs } from "node:fs";

// Setup CLI
program
  .name("cat")
  .description("Concatenate files and print on the standard output")
  .option("-n, --number", "number all output lines")
  .option("-b, --number-nonblank", "number nonempty output lines")
  .argument("<path...>", "file(s) to read");

program.parse();

const files = program.args;
const { number, numberNonblank } = program.opts();

// Validate input
if (files.length === 0) {
  console.error("cat: missing file operand");
  process.exit(1);
}

let lineNumber = 1;

// Helper to print lines with optional numbering
function printLine(line, shouldNumber) {
  if (shouldNumber) {
    console.log(`${String(lineNumber).padStart(6)}\t${line}`);
    lineNumber++;
  } else {
    console.log(line);
  }
}

for (const file of files) {
  let content;
  try {
    content = await fs.readFile(file, "utf8");
  } catch (err) {
    console.error(`cat: ${file}: ${err.message}`);
    continue;
  }

  const lines = content.split("\n");

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];

    // Avoid printing an extra line if file ends with \n
    if (i === lines.length - 1 && line === "") {
      break;
    }

    const isBlank = line.trim() === "";

    if (numberNonblank) {
      printLine(line, !isBlank);
    } else if (number) {
      printLine(line, true);
    } else {
      printLine(line, false);
    }
  }
}
