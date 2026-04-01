#!/bin/bash

set -euo pipefail
$ grep "Doctor" -i dialogue.txt
Doctor: Hello
Patient: Hello Doctor
Doctor: What's wrong today?
Doctor: That sounds frustrating. When did this start?
Doctor: Say "Hi".
Doctor: You didn't say hello
Doctor: You're welcome, goodbye
Patient: I went to the doctor!
Spouse: I'm glad you saw the Doctor: did they cure you?

# TODO: Write a command to output every line in dialogue.txt that contains the word Doctor (regardless of case).
# The output should contain 9 lines.
