import { program } from "commander";
import process from "node:process";
import { promises as fs } from "node:fs";

program
  .name("Implement wc")
  .description("Implements a version of the wc command")
  .option("-l, --line", "Counts file lines")
  .option("-c, --char", "Counts characters in file")
  .option("-w, --word", "Counts words in file")
  .argument("[paths...]", "The path/s to process")
  .parse(process.argv);

const args = program.args;

const lineOption = program.opts().line;
const charOption = program.opts().char;
const wordOption = program.opts().word;

async function countLinesWordsCharsInFile(path) {
  const content = await fs.readFile(path, { encoding: "utf-8" });

  const lines = content.split("\n")
  lines[lines.length - 1] === "" ? lines.pop() : lines;

  const words = lines.flatMap((element) =>
    element.split(" ").filter((word) => word !== "")
  );

  const chars = content.split("");

  const numberOfLines = lines.length;
  const numberOfWords = words.length;
  const numberOfChars = chars.length;

  if (lineOption && charOption) {
    return `${numberOfLines} ${numberOfChars} ${path}`;
  }

  if (lineOption && wordOption) {
    return `${numberOfLines} ${numberOfWords} ${path}`;
  }

  if (wordOption && charOption) {
    return `${numberOfWords} ${numberOfChars} ${path}`;
  }

  if (lineOption) {
    return `${numberOfLines} ${path}`;
  }

  if (charOption) {
    return `${numberOfChars} ${path}`;
  }

  if (wordOption) {
    return `${numberOfWords} ${path}`;
  }

  return `${numberOfLines} ${numberOfWords} ${numberOfChars} ${path}`;
}

async function processFilesAndDisplayCounts() {
  const fileCounts = await Promise.all(args.map(countLinesWordsCharsInFile));
  fileCounts.forEach((fileCount) => console.log(fileCount));

  const aggregatedFilesData = aggregateFileData(fileCounts);

  if (aggregatedFilesData !== 0 && lineOption && !(wordOption || charOption)) {
    console.log(`${aggregatedFilesData[0]} total`);
    return;
  }

  if (aggregatedFilesData !== 0 && charOption && !(wordOption || lineOption)) {
    console.log(`${aggregatedFilesData[0]} total`);
    return;
  }

  if (aggregatedFilesData !== 0 && wordOption && !(lineOption || charOption)) {
    console.log(`${aggregatedFilesData[0]} total`);
    return;
  }


  if (
    aggregatedFilesData !== 0 &&
    ((lineOption && charOption) || (lineOption && wordOption) || (wordOption && charOption))
  ) {
    console.log(`${aggregatedFilesData[0]} ${aggregatedFilesData[1]} total`);
    return;
  }

  aggregatedFilesData !== 0
    ? console.log(
        `${aggregatedFilesData[0]} ${aggregatedFilesData[1]} ${aggregatedFilesData[2]} total`
      )
    : null;
}

/**
 * Aggregates numerical data from an array of file content strings.
 *
 * @param {string[]} files - An array of strings, each representing the content of a file.
 * Each string should contain space-separated numbers.
 * @returns {number[]|number} - An array of sums for each column of numbers if there are multiple files,
 * or 0 if there is only one file.
 */
function aggregateFileData(fileCounts) {
  const digits = fileCounts.map((element) =>
    element.split(" ").slice(0, -1).map(Number)
  );
  const sums =
    digits.length > 1
      ? digits[0].map((_, colIndex) =>
          digits.reduce((sum, row) => sum + row[colIndex], 0)
        )
      : digits[0];
  return sums;
}

processFilesAndDisplayCounts();
