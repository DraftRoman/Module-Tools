import { program } from "commander";
import * as fs from "node:fs/promises";

program
  .name("cat")
  .description("Reads file(s) and writes them to the standard output")
  .argument("<paths...>", "The file path(s) to process")
  .option("-n", "Number the output lines, starting at 1.")
  .option("-b", "Number only non-blank output lines, starting at 1.");

program.parse();

try {
  const filePaths = program.args;

  const options = program.opts();

  for (const filePath of filePaths) {
    const file = await fs.open(filePath);

    let lineNum = 1;

    try {
      for await (const line of file.readLines()) {
        const isBlank = line.trim() === "";
        const shouldNumber = options.n || (options.b && !isBlank);

        console.log(shouldNumber ? `${lineNum}  ${line}` : line);

        if (shouldNumber) lineNum++;
      }
    } finally {
      await file.close();
    }
  }
} catch (err) {
  console.error(err.message);
}
