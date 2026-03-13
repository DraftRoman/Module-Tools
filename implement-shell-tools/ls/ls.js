import { program } from "commander";
import * as fs from "node:fs/promises";

program
  .name("ls")
  .description("List directory contents")
  .argument(
    "[paths...]",
    "The file path to process (defaults to current directory)",
  )
  .option("-a", "Include directory entries whose names begin with a dot ('.').")
  .option("-1", "Force output to be one entry per line.");

program.parse();

try {
  let filePaths = program.args;
  if (!filePaths || filePaths.length === 0) {
    filePaths = ["."];
  }

  const options = program.opts();
  const includeHidden = Boolean(options.a);
  const onePerLine = Boolean(options["1"]);

  const result = { files: [], dirs: {} };

  for (const filePath of filePaths) {
    const stats = await fs.stat(filePath);
    if (stats.isFile()) result.files.push(filePath);
    if (stats.isDirectory()) {
      result.dirs[filePath] = await fs.readdir(filePath);
    }
  }

  const filterHidden = (files) => files.filter((file) => !file.startsWith("."));

  const getVisibleEntries = (files) =>
    includeHidden ? files : filterHidden(files);

  const formatEntries = (files) => {
    if (files.length === 0) return;
    console.log(files.join(onePerLine ? "\n" : "\t"));
  };

  result.files = getVisibleEntries(result.files);

  if (filePaths.length === 1) {
    let entries = [...result.files];

    for (const [dir, contents] of Object.entries(result.dirs)) {
      const filtered = getVisibleEntries(contents);
      entries = entries.concat(filtered);
    }
    formatEntries(entries);
  } else {
    formatEntries(result.files);

    for (const [dir, contents] of Object.entries(result.dirs)) {
      console.log("\n" + dir + ":");
      const filtered = getVisibleEntries(contents);
      formatEntries(filtered);
    }
  }
} catch (err) {
  console.error(err.message);
}
