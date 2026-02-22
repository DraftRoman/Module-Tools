import { promises as fs } from "node:fs";

async function cleanInput(listOfFiles) {
	let cleanLinesArr = [];
	for (const file of listOfFiles) {
		const grabbedText = await fs.readFile(file, "utf-8");
		const splitLines = grabbedText.split("\n");
		cleanLinesArr.push(...splitLines);
	}
	return cleanLinesArr;
}

function takeSpecifiedAction(cleanLinesArr, flag) {
	let countingOnlyFullLines = 1;

	for (const file of cleanLinesArr) {
		// Task: We recommend you start off supporting no flags, then add support for `-n`, then add support for `-b`.
		if (!flag) {
			console.log(file);
		} else if (flag === "-n") {
			console.log(`${countingOnlyFullLines} ${file}`);
			countingOnlyFullLines += 1;
		} else if (flag === "-b") {
			if (file === "") {
				console.log("");
			} else {
				console.log(`${countingOnlyFullLines} ${file}`);
				countingOnlyFullLines += 1;
			}
		} else {
			console.log("incorrect flag");
		}
	}
}
