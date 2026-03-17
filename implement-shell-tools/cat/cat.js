import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

// configure the CLI program with its name, description, arguments, options, and actions (the help instructions)
program
    .name("cat")
    .description("An alternative to the 'cat' command")
    .argument("<files...>", "The file(s) to process") 
    .option("-n, --number", "Number all output lines")
    .option("-b, --number-nonblank", "Number non-blank output lines")
    .action(async (files, options) => {
        try {
            await newCat(files, options);
        } catch (err) {
            console.error(`Error: ${err.message}`);
        }
    });

program.parse(process.argv);

//helper function to format output
function printLine(line, lineNumber, padWidth) {
    if (lineNumber !== null) {
        console.log(`${lineNumber.toString().padStart(padWidth, '  ')}  ${line}`);
    } else {
        console.log(line);
    }
}

async function newCat(files, options) {
    let lineNumber = 1;
    const padWidth = 6;

    for (const file of files) {
        // read each file into a single text string
        try {
            const data = await fs.readFile(file, "utf8");
            // split that string into an array at \n where each element is a line from the file
            // e.g. lines = ["Line 1", "Line 2", "Line 3"]
            const lines = data.split("\n")

            // remove trailing blank line caused by a trailing newline
            if (lines[lines.length - 1] === "") {
                lines.pop();
            }

            lines.forEach(line => {
                //line trim: truthy = text, falsy = blank
                if (options.numberNonblank && line.trim()) {
                    // number non-blank lines only
                    printLine(line, lineNumber++, padWidth);
                }  else if (options.number){
                    // number all lines
                    printLine(line, lineNumber++, padWidth);
                } else {
                    // neither flag, print normally
                   printLine(line, null, padWidth)
                }
            });
        } catch (err) {
            console.error(`Error reading file ${file}: ${err.message}`);
        }
    }
}