#!/bin/bash

set -euo pipefail

$ awk '/London/ {print $1,$NF}' scores-table.txt 
Ahmed 4
Basia 6
Leila 1

NF = total number of fields in the line

# TODO: Write a command to output just the names of each player in London along with the score from their last attempt.
# Your output should contain 3 lines, each with one word and one number on it.
# The first line should be "Ahmed 4".
