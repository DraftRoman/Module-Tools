import process from "node:process";
import { promises as fs } from "node:fs";

//  `ls -1`
async function showAllFilesInDir(directory) {
	const listOfFiles = await fs.readdir(directory);

	for (const eachFile of listOfFiles) {
		if (eachFile[0] !== ".") console.log(eachFile);
	}
}

// `ls -1 sample-files`
async function showVisibleInSampleFiles() {
	const listOfFiles = await fs.readdir("sample-files");

	for (const eachFile of listOfFiles) {
		if (eachFile[0] !== ".") {
			console.log(eachFile);
		}
	}
}

// `ls -1 -a sample-files`
async function showAllInSampleFiles() {
	const listOfFiles = await fs.readdir("sample-files");

	for (const eachFile of listOfFiles) {
		console.log(eachFile);
	}
}

const argv = process.argv.slice(2);

if (argv.includes("-a")) {
	await showAllInSampleFiles();
} else if (argv.includes("sample-files")) {
	await showVisibleInSampleFiles();
} else {
	await showAllFilesInDir(".");
}
