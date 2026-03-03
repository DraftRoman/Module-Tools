import { program } from "commander";
import { promises as fs } from "node:fs";
import path from "node:path";

program
  .name("my-ls")
  .description("List files in a directory (simplified ls implementation)")
  .argument("[paths...]", "One or more file or directory paths")
  .option("-l, --longList", "Long listing format", false)
  .option("-a, --all", "Include hidden files", false);

program.parse();

// CHANGED: apply default value for paths here if none are provided
let filePaths = program.args.length > 0 ? program.args : ['.']; 
const options = program.opts();

const showLong = options.longList;
const showAll = options.all;

// Helper function to convert mode to rwxrwxrwx string
function formatPermissions(mode, isDir) {
  const typeChar = isDir ? 'd' : '-';
  const perms = [0, 1, 2].map(i => {
    const shift = 6 - i * 3;
    const r = (mode >> shift) & 4 ? 'r' : '-';
    const w = (mode >> shift) & 2 ? 'w' : '-';
    const x = (mode >> shift) & 1 ? 'x' : '-';
    return r + w + x;
  }).join('');
  return typeChar + perms;
}

(async () => {
  for (const inputPath of filePaths) {
    try {
      const stat = await fs.stat(inputPath);

      if (stat.isFile()) {
        if (showLong) {
          const perms = formatPermissions(stat.mode, false);
          console.log(`${perms}  ${stat.size.toString().padStart(6)}  ${inputPath}`);
        } else {
          console.log(inputPath);
        }
      } else if (stat.isDirectory()) {
        const entries = await fs.readdir(inputPath, { withFileTypes: true });

        const filtered = showAll
          ? entries
          : entries.filter((entry) => !entry.name.startsWith("."));

        for (const entry of filtered) {
          const fullPath = path.join(inputPath, entry.name);
          const entryStat = await fs.stat(fullPath);
          if (showLong) {
            const perms = formatPermissions(entryStat.mode, entryStat.isDirectory());
            console.log(`${perms}  ${entryStat.size.toString().padStart(6)}  ${entry.name}`);
          } else {
            console.log(entry.name);
          }
        }
      }
    } catch (err) {
      console.error(`Error reading "${inputPath}": ${err.message}`);
      process.exit(1);
    }
  }
})();
