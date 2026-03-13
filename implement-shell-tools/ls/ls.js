import { program } from "commander";
import * as fs from "node:fs/promises";

program
  .name("ls")
  .description("List directory contents")
  .argument(
    "[path]",
    "The file path to process (defaults to current directory)",
  )
  .option("-a", "Include directory entries whose names begin with a dot ('.').")
  .option("-1", "Force output to be one entry per line.");

program.parse();

try {
  const options = program.opts();
  const [filePathArg] = program.args;

  const filePath = filePathArg || process.cwd();
  let files = await fs.readdir(filePath);

  if (!options.a) files = files.filter((file) => !file.startsWith("."));

  if (options["1"]) {
    for (const file of files) {
      console.log(file);
    }
  } else {
    console.log(...files);
  }
} catch (err) {
  console.error(err.message);
}
