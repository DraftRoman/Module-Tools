import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program
  .name("ls")
  .description("This is a program to display the childern of a directory.")
  .option("-1, --one", "This is to list all the children of a directory, one per line.")
  .option("-a", "The flag to list the children of a directory one per line in long format.")
  .argument("<filepath>")

program.parse(process.argv);

const opts = program.opts();
const args = program.args;

if (args.length != 1) {
  console.error(`Expected exactly 1 argument (a path) to be passed but got ${args.length}.`);
  process.exit(1);
}

const content = await fs.readdir(args[0], "utf-8");

const results = content.join(' ')
// const regex = '/\n/'

const filtered = content.filter((word) => word.charAt(0) !== '.')

if (opts.one) {
  console.log(filtered.join('\n'))
}
else if (opts.a) {
  console.log(content.join(' '));
}
else {
  console.log(filtered.join(' '))
}

