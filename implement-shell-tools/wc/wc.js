import { program } from "commander";
import * as fs from "node:fs/promises";

//*** TODO ***
// * Format results
// * Add optional flags

program
  .name("wc")
  .description("word, line and byte count")
  .argument("<paths...>", "The file path(s) to process");

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
  console.log(results);
} catch (err) {
  console.error(err.message);
}
