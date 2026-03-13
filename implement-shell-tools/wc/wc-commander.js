import {program} from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";
import { glob } from "glob";

program
    .name("content counter")
    .description("Counts lines, words, or characters in a file or files of a directory.")
    .option("-l,--lines","Options for l:Lines.")
    .option("-w,--words","Options for w:words.")
    .option("-c","Options for c:characters.")
    .argument("<path...>","The file or directory to process");

program.parse();

const argv = program.args;

const options = program.opts();

const result = []; 
let totalLines = 0;
let totalWords = 0;
let totalChars = 0;

for (const file of argv){

  //1.  Read each file

  const content = await fs.readFile(file,"utf-8");
  // 2. calculate values
  const lines = content.split(/\n/g).length - 1 ;
  const words = content.trim().split(/\s+/).length;
  const chars = content.split("").length;
  // variable to pile up final line results according options
  const thisLine = [];
  if (options.lines){ thisLine.push(lines.toString().padStart(8)) };
  if (options.words){ thisLine.push(words.toString().padStart(8)) };
  if (options.c){ thisLine.push(chars.toString().padStart(8)) };
  if (!options.lines && !options.words && !options.c){ thisLine.push(lines.toString().padStart(8),words.toString().padStart(8),chars.toString().padStart(8)) };
  result.push(`${thisLine.join("")} ${file}`)
  // 3. add results 
  // variables to accumulate the total
  totalLines += lines;
  totalWords += words;
  totalChars += chars;
// 4. add total results if several files
}
if (argv.length>1){
  const finalLine = [];
  finalLine.push(totalLines.toString().padStart(8)),
  finalLine.push(totalWords.toString().padStart(8)),
  finalLine.push(totalChars.toString().padStart(8));
  result.push(`${finalLine.join("")} total`)
}
// 5. show results
const output = result.join('\n');
console.log(output)




