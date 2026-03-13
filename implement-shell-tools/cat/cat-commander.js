import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program
    .name("read-files-content")
    .description("Read the content of a file (simulating cat command)")
    .option("-n, --number","Number of lines")
    .option("-b","Number of no-blanks lines")
    .argument("<path...>","The file path to process"); //file

program.parse();

const argv = program.args;

if (argv.length === 0) {
    console.error(`Expected file path(s),passed but got ${argv.length}.`);
    process.exit(1);
}

//const path = argv[0];
for (const path of argv){
    const option = program.opts();
    const content = await fs.readFile(path, "utf-8");
    if (option.number){
        // split content
        let lines = content.split(/\n/);
        // removes last line
        if (lines[lines.length - 1] === ""){
            lines = lines.slice(0,-1);
        }
        lines
            .map((line,index) => `${(index + 1).toString().padStart(6)}\t${line}`)
            .forEach(line => console.log(line))

        } else if (option.b){
            let lines = content.split("\n");
            let linesCounter = 0;
            if (lines[lines.length - 1] === ""){
                lines = lines.slice(0,-1);
            }
            lines
            .map((line) => {
                if (line.trim().length > 0) { 
                    linesCounter++;
                    return `${linesCounter.toString().padStart(6)}\t${line}`
                }else{
                    return `${line}`
                    }}
                )
            .forEach(line => console.log(line))
        }else {
            const output = content.endsWith("\n") ? content.slice(0,-1) : content;
            console.log(output);
    }
}
