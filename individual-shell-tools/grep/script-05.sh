#!/bin/bash

set -euo pipefail
$ grep "cure" -iB 1 dialogue.txt
Doctor: You didn't say hello
Patient: I seem to be cured!
--
Patient: I went to the doctor!
Spouse: I'm glad you saw the Doctor: did they cure you?

# TODO: Write a command to output every line in dialogue.txt that contains the string "cure", as well as the line before that line.
# The output should contain two pairs of two lines of text (with a separator between them).
