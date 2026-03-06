#!/bin/bash

set -euo pipefail

# TODO: Write a command to output the number of lines in dialogue.txt that contain the word Doctor (regardless of case).
grep -ic "Doctor" dialogue.txt
# The output should be exactly the number 9.
