#!/usr/bin/env node
const fs = require("node:fs");
//shared line counter across all files(matches cat -n)
let globalLineCounter = 1;

function printFile(filePath, options) {
  try {
    const content = fs.readFileSync(filePath, "utf-8");
    const lines = content.split("\n");

    lines.forEach((line) => {
      let prefix = "";

      if (options.numberMode === "non-empty") {
        //-b option: number non-empty lines
        if (line.trim() !== "") {
          prefix = `${String(globalLineCounter).padStart(6)}\t`;
          globalLineCounter++;
        }
      } else if (options.numberMode === "all") {
        prefix = `${String(globalLineCounter).padStart(6)}\t`;
        globalLineCounter++;
      }

      process.stdout.write(`${prefix}${line}\n`);
    });
  } catch (error) {
    console.error(`cat: ${filePath}: ${error.message}`);
  }
}

function main() {
  const args = process.argv.slice(2);

  const options = {
    numberMode: "off",
  };

  const files = [];
  args.forEach((arg) => {
    if (arg === "-n") {
      options.numberMode = "all";
    } else if (arg === "-b") {
      options.numberMode = "non-empty";
    } else {
      files.push(arg);
    }
  });

  if (files.length === 0) {
    console.log("cat: missing file operand");
    process.exit(1);
  }

  files.forEach((file) => {
    printFile(file, options);
  });
}

main();
