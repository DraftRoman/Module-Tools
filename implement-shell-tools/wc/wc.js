import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

// configure the CLI program with its name, description, arguments, options, and actions (the help instructions)
program
  .name("wc")
  .description("An alternative to the 'wc' command")
  .argument("<files...>", "The file(s) to count lines/words/bytes")
  .option("-l, --lines", "Print the newline counts")
  .option("-w, --words", "Print the word counts")
  .option("-c, --bytes", "Print the byte counts")
  .action(async (files, options) => {
        try {
            // call newWc for all files
            await newWc(files, options)
        } catch (err) {
        console.error(`Error: ${err.message}`);
        }
  });

  program.parse(process.argv);

//helper function to format string for output
function formatCount(count) {
    const paddingStart = 3
    return count.toString().padStart(paddingStart);
}


// helper function to print the wc outputs per case
function printWcOutput(lineCount, wordCount, byteCount, file, options, noFlags) {
    const parts = [];

    if (noFlags || options.lines) parts.push(formatCount(lineCount));
    if (noFlags || options.words) parts.push(formatCount(wordCount));
    if (noFlags || options.bytes) parts.push(formatCount(byteCount));
    
    parts.push(file);
    console.log(parts.join(" "));
}

async function newWc(files, options) {

    const noFlags =
    !options.lines &&
    !options.words &&
    !options.bytes;

    // set the counts variables
    let totalLines = 0;
    let totalWords = 0;
    let totalBytes = 0;

    for (const file of files) {
        try {
            // read each file into a single text string
            const content = await fs.readFile(file, "utf8");

            // count lines by splitting on '\n' and subtracting 1 because
            // each newline creates an extra array element, so length-1 equals the number of newline characters
            const lineCount = content.split("\n").length - 1;

            // .filter(Boolean) ensures that falsy values like "" (empty string), null, undefined, 0, false are removed
            const wordCount = content.split(/\s+/).filter(Boolean).length;
        
            // calculates the number of bytes the file uses when encoded as UTF-8.
            // different than just counting chars as some chars (like emojis, accented letters, etc) take more than 1 byte
            const byteCount = Buffer.byteLength(content, "utf8");

            // update the count
            totalLines += lineCount;
            totalWords += wordCount;
            totalBytes += byteCount;

            printWcOutput(lineCount, wordCount, byteCount, file, options, noFlags);     
        } catch (err) {
            console.error(`Error reading file ${file}: ${err.message}`);
        }
    }
    if (files.length > 1) {
    // print the totals as wc does
    printWcOutput(totalLines, totalWords, totalBytes,  "total", options, noFlags);
}
}
