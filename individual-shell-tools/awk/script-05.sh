#!/bin/bash

set -euo pipefail

# TODO: Write a command to output just the names of each player along with the number of times they've played the game.
awk '{columns_num = NF - 2; print $1, columns_num }' scores-table.txt
# Your output should contain 6 lines, each with one word and one number on it.
# The first line should be "Ahmed 3".
