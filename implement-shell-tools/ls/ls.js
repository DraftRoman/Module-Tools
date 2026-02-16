import process from "node:process";
import { promises as fs } from "node:fs";
import { program } from "commander";

program
  .name("Implement ls")
  .description("Implements a version of the ls command")
  .option("-1, --one", "Output all files and directories each in a line")
  .option("-a, --hidden", "Output hidden files/directories")
  .argument("[paths...]", "the paths to be processed")
  .parse(process.argv);

/**
 * Reads the contents of the specified directories and outputs the file names.
 * Supports options for displaying hidden files and listing each file on a new line.
 *
 * @param {string[]} filePaths - The paths to be processed. Defaults to the current directory if no argument is provided.
 * @param {boolean} one - If true, outputs each file and directory on a new line.
 * @param {boolean} hidden - If true, includes hidden files and directories in the output.
 */

const filePaths = program.args.length ? program.args : ["."];

const outputOnePerLine = program.opts().one;
const includeHiddenFiles = program.opts().hidden;

async function listDirectoryContents(filePath) {
  try {
    const files = await fs.readdir(filePath, { withFileTypes: true }); // is returned as a Dirent
    const output = [];

    files.forEach((file) => {
      if (includeHiddenFiles || !file.name.startsWith(".")) {
        output.push(file.name);
      }
    });

    if (includeHiddenFiles) {
      output.unshift(".", "..");
    }

    outputOnePerLine === true
      ? output.forEach((file) => console.log(file))
      : console.log(output.join(" "));
  } catch (err) {
    console.error(`Error reading directory ${filePath}:`, err.message);
  }
}

//filePaths.map(listDirectoryContents);fi
filePaths.forEach(listDirectoryContents);