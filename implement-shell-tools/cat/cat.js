import { program } from "commander";
import * as fs from "node:fs/promises";

program
  .name("cat")
  .description("Reads file and writes it to the standard output")
  .argument("<path>", "The file path to process")
  .option("-n", "Number the output lines, starting at 1.")
  .option("-b", "Number only non-blank output lines, starting at 1.");

program.parse();

try {
  const [filePath] = program.args;
  const options = program.opts();

  const file = await fs.open(filePath);

  let lineNum = 1;
  for await (const line of file.readLines()) {
    const isBlank = line.trim() === "";
    const shouldNumber = options.n || (options.b && !isBlank);

    console.log(shouldNumber ? `${lineNum}  ${line}` : line);

    if (shouldNumber) lineNum++;
  }
} catch (err) {
  console.error(err.message);
}
