#!/usr/bin/env node

// A simple reimplementation of `cat` in NodeJS.
// Supports:
//   node cat.js sample-files/1.txt
//   node cat.js -n sample-files/1.txt
//   node cat.js -b sample-files/3.txt
//   node cat.js sample-files/*.txt
//
// -n : number all lines
// -b : number non-empty lines

const fs = require("fs");
const path = require("path");

// -------- argument parsing --------
const args = process.argv.slice(2);

if (args.length === 0) {
  console.error("Usage: node cat.js [-n | -b] <file> [<file> ...]");
  process.exit(1);
}

let numberAll = false;
let numberNonBlank = false;
let fileArgs = [];

// Very small argument parser:
// We only care about -n or -b as the FIRST arg (like the coursework examples).
if (args[0] === "-n") {
  numberAll = true;
  fileArgs = args.slice(1);
} else if (args[0] === "-b") {
  numberNonBlank = true;
  fileArgs = args.slice(1);
} else {
  fileArgs = args;
}

if (fileArgs.length === 0) {
  console.error("cat.js: no input files");
  process.exit(1);
}

// -------- helper functions --------

/**
 * Format a single line with the correct line number, if needed.
 *
 * @param {string} line - line text (without the trailing newline)
 * @param {number} currentLineNumber - global line counter
 * @param {boolean} numberAll - true if -n
 * @param {boolean} numberNonBlank - true if -b
 * @returns {{ text: string, nextLineNumber: number }}
 */
function formatLine(line, currentLineNumber, numberAll, numberNonBlank) {
  let output = "";
  let nextLineNumber = currentLineNumber;

  const isBlank = line === "";

  if (numberAll) {
    // Always number every line
    output =
      currentLineNumber.toString().padStart(6, " ") + "\t" + line;
    nextLineNumber++;
  } else if (numberNonBlank) {
    // Number only non-blank lines
    if (isBlank) {
      output = line; // No number, just the blank line
    } else {
      output =
        currentLineNumber.toString().padStart(6, " ") + "\t" + line;
      nextLineNumber++;
    }
  } else {
    // No numbering
    output = line;
  }

  return { text: output, nextLineNumber };
}

/**
 * Print a file to stdout according to the options.
 *
 * @param {string} filePath
 * @param {number} startLineNumber
 * @returns {number} next line number
 */
function printFile(filePath, startLineNumber) {
  let content;

  try {
    content = fs.readFileSync(filePath, "utf8");
  } catch (err) {
    console.error(`cat.js: ${filePath}: ${err.message}`);
    return startLineNumber;
  }

  const lines = content.split("\n");
  let lineNumber = startLineNumber;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const { text, nextLineNumber } = formatLine(
      line,
      lineNumber,
      numberAll,
      numberNonBlank
    );
    lineNumber = nextLineNumber;

    // Re-add the newline we lost when splitting
    process.stdout.write(text);

    // Avoid adding an extra newline at very end if the file
    // doesn't end with \n — Node's split keeps the last segment.
    if (i < lines.length - 1 || content.endsWith("\n")) {
      process.stdout.write("\n");
    }
  }

  return lineNumber;
}

// -------- main execution --------

let globalLineNumber = 1;

for (const file of fileArgs) {
  // Shell expands *.txt, so here we just get each file path.
  const resolvedPath = path.resolve(file);
  globalLineNumber = printFile(resolvedPath, globalLineNumber);
}
