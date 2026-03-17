import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

// configure the CLI program with its name, description, arguments, options, and actions (the help instructions)
program
    .name("ls")
    .description("An alternative to the 'ls' command")
    .argument("[directory]", "The directory to list")
    // Commander stores -1 as a string key that is accessed using options['1']
    .option("-1", "List all files, one per line")
    .option("-a, --all", "Include hidden files (those starting with .) in the listing")
    .action(async (directory, options) => {
        try {
            // default to current directory if none is specified
            const dir = directory || ".";

            await newLs(dir, options['1'], options.all);
        } catch (err) {
            console.error(`Error: ${err.message}`);
        }
    });

program.parse(process.argv);


// filter files based on visibility (includeHidden = true includes all files)
function filterFiles(entries, includeHidden) {
    return entries.filter(name =>
        includeHidden ? true : !name.startsWith(".")
    );
}

// sort entries: directories first, then files,
function sortEntries(entries) {
    const dirs = entries.filter(entry => {
        try {
            return fs.statSync(entry).isDirectory();
        } catch (err) {
            return false;
        }
    });

    const files = entries.filter(entry => {
        try {
            return fs.statSync(entry).isFile();
        } catch (err) {
            return false;
        }
    });
    // localeCompare = take into account rules of system language/region for ordering 
    // undefined = uses the system default, numeric = regular number sorting, base = ignore case & accents
    return entries.sort((a, b) =>
        a.localeCompare(b, undefined, { numeric: true, sensitivity: "base" })
    );
}


// print each entry on its own line (used for -1 flag)
function printEntries(entries) {
    entries.forEach(entry => console.log(entry));
}


async function newLs(directory, oneFlag, allFlag) {
    try {
        // check if path exists and determine if file or directory
        const stats = await fs.stat(directory);
        
        // if a file, just print the name
        if (stats.isFile()) {
            console.log(directory);
            return;
        }

        // reads directory contents 
        const entries = await fs.readdir(directory);

        // filter out hidden files if no -a flag
        const filteredEntries = filterFiles(entries, allFlag);

        // sort the entries using the sortEntries helper
        const sortedEntries = sortEntries(filteredEntries);
        
        // print entries based on -1 flag
        if (oneFlag) {
            printEntries(sortedEntries); // one per line
        } else {
            console.log(sortedEntries.join("  ")); // all on one line, separated by spaces
        }
    } catch (err) {
        console.error(`ls: cannot access '${directory}': ${err.message}`);
    }
}