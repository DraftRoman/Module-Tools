import process from "node:process";
import { promises as fs } from "node:fs";

//from coursework
// const content = await fs.readFile(path, "utf-8");
// const countOfWordsContainingEs = content
//   .split(" ")
//   .filter((word) => word.includes("e"))
//   .length;
// console.log(countOfWordsContainingEs);

function calculateCounts(inputFiles) {
	return {
		lines: inputFiles.split("\n").length - 1,
		words: inputFiles.split(/\s+/).filter((w) => w !== "").length,
		bytes: inputFiles.length,
	};
}

// * `wc -l sample-files/3.txt`
// * `wc -l sample-files/*`
async function countLines(listOfFiles) {
	for (const file of listOfFiles) {
		const content = await fs.readFile(file, "utf-8");

		// const linesNumbered = content.split('\n').length-1
		const counts = calculateCounts(content);
		console.log(`${counts.lines} ${file}`);
	}
}

// * `wc -w sample-files/3.txt`
async function countWords(listOfFiles) {
	for (const file of listOfFiles) {
		const content = await fs.readFile(file, "utf-8");

		// const wordsCounted = content.split(" ").filter(word => word !== "").length;
		// console.log(`${wordsCounted} ${file}`);
		const counts = calculateCounts(content);
		console.log(`${counts.words} ${file}`);
	}
}

// * `wc -c sample-files/3.txt`
async function countBytes(listOfFiles) {
	for (const file of listOfFiles) {
		const content = await fs.readFile(file, "utf-8");
		// const bytesCounted = content.length;
		const counts = calculateCounts(content);
		console.log(`${counts.bytes} ${file}`);
	}
}

// * `wc sample-files/*`
async function countAll(listOfFiles) {
	for (const file of listOfFiles) {
		const content = await fs.readFile(file, "utf-8");
		const counts = calculateCounts(content);
		console.log(`${counts.lines} ${counts.words} ${counts.bytes} ${file}`);
	}
}

const argv = process.argv.slice(2);
const files = argv.filter((arg) => !arg.startsWith("-"));

if (argv.includes("-l")) {
	await countLines(files);
} else if (argv.includes("-w")) {
	await countWords(files);
} else if (argv.includes("-c")) {
	await countBytes(files);
} else {
	await countAll(files);
}
