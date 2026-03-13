import { program } from "commander";
import * as fs from "node:fs/promises";

program
  .name("wc")
  .description("word, line and byte count")
  .argument("<paths...>", "The file path(s) to process.")
  .option(
    "-l, --lines",
    "The number of lines in each input file is written to the standard output.",
  )
  .option(
    "-w, --words",
    "The number of words in each input file is written to the standard output.",
  )
  .option(
    "-c --bytes",
    "The number of bytes in each input file is written to the standard output.",
  );

program.parse();

try {
  const filePaths = program.args;
  const results = {};

  for (const filePath of filePaths) {
    const file = await fs.open(filePath);
    const stats = await fs.stat(filePath);
    const count = { lines: 0, words: 0, bytes: stats.size };

    try {
      for await (const line of file.readLines()) {
        count.lines++;
        count.words += line.trim().split(/\s+/).length;
      }
    } finally {
      await file.close();
    }
    results[filePath] = count;
  }

  if (filePaths.length > 1) {
    const total = { lines: 0, words: 0, bytes: 0 };
    for (const file of Object.values(results)) {
      total.lines += file.lines;
      total.words += file.words;
      total.bytes += file.bytes;
    }
    results["total"] = total;
  }

  const options = program.opts();
  const noOptionsProvided = !Object.keys(options).length;
  const selectedOptionKeys = [...Object.keys(options)];

  noOptionsProvided
    ? console.table(results)
    : console.table(results, selectedOptionKeys);
} catch (err) {
  console.error(err.message);
}
