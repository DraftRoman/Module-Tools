#!/usr/bin/env node
import { program } from "commander";
import fs from "fs";
import path from "path";

// Define CLI
program
  .name("ls-clone")
  .description("A simple implementation of ls")
  .option("-1", "list one file per line")
  .option("-a", "include hidden files")
  .argument("[dirs...]", "directories to list", "."); // default is current dir

program.parse();

const options = program.opts();
const dirs = program.args.length ? program.args : ["."];
const onePerLine = options["1"];
const showAll = options.a;

for (const dir of dirs) {
  let files;
  try {
    files = fs.readdirSync(dir);
  } catch (err) {
    console.error(`ls-clone: cannot access '${dir}': No such file or directory`);
    continue;
  }

  if (!showAll) {
    files = files.filter(name => !name.startsWith("."));
  }

  // Output
  if (onePerLine) {
    files.forEach(f => console.log(f));
  } else {
    console.log(files.join("  "));
  }
}
