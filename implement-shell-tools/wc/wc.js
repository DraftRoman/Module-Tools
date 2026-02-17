import { program } from "commander";
import process from "node:process";
import { promises as fs } from "node:fs";


program
    .name("wc")
    .description("Counts lines, words, and bytes in files")
    .option("-l", "print the newline counts")
    .option("-w", "print the word counts")
    .option("-c", "print the byte counts")
    .argument("<files...>", "Files to count");   

program.parse();

const files = program.args;
const opts = program.opts();


if (files.length < 1) {
    console.error("Please specify one or more files.");
    process.exit(1);
}


async function wcOneFile(filename) {
    try {
        const content = await fs.readFile(filename, "utf-8");


        const lines = content === "" ? 0 : content.split('\n').length;


        const words = content.trim().split(/\s+/).filter(Boolean).length;

        // Count bytes (characters in UTF-8 encoding)
        const bytes = Buffer.byteLength(content, "utf8");

        return { lines, words, bytes, filename, error: false };
    } catch (err) {
        return { filename, error: true };
    }
}


function printCounts({ lines, words, bytes, filename, error }) {
    if (error) {
        console.error(`Could not read file: ${filename}`);
        return;
    }
    
    const showAll = !opts.l && !opts.w && !opts.c;
    let out = [];
    if (opts.l || showAll) out.push(lines);
    if (opts.w || showAll) out.push(words);
    if (opts.c || showAll) out.push(bytes);
    out.push(filename);
    console.log(out.join(" "));
}


let totalLines = 0, totalWords = 0, totalBytes = 0;

for (const file of files) {


    const result = await wcOneFile(file);

    printCounts(result);


    if (!result.error) {
        totalLines += result.lines;
        totalWords += result.words;
        totalBytes += result.bytes;
    }
}


if (files.length > 1) {
    const showAll = !opts.l && !opts.w && !opts.c;
    let out = [];
    if (opts.l || showAll) out.push(totalLines);
    if (opts.w || showAll) out.push(totalWords);
    if (opts.c || showAll) out.push(totalBytes);
    out.push("total");
    console.log(out.join(" "));
}
