import { program } from "commander";
import * as fs from "node:fs/promises";

program
  .name("cat")
  .description("Reads file and writes it to the standard output")
  .argument("<path>", "The file path to process");

program.parse();

try {
  const [filePath] = program.args;
  const contents = await fs.readFile(filePath, { encoding: "utf8" });
  console.log(contents);
} catch (err) {
  console.error(err.message);
}
