#!/bin/bash

set -euo pipefail

# TODO: Write a command to output input.txt with one fix:
# If a comma in input.txt is not followed by a space, add a space after.
# If there is already a space after a comma, do not add an additional space.
# The output should contain 11 lines.
# Line 3 should be "It contains many lines, and there are some things you may want to do with each of them.".
# Line 11 should be "We also should remember, when we go shopping, to get 4 items: oranges, cheese, bread, olives.".
$ sed -E 's/,([^ ])/,\1/g' input.txt
This is a sample file for experimenting with sed.

it contains many lines, and there are some things you may want to do with each of them.

We will include some score information:
37 Alisha
15 Jacob
7 Pietro
3 Katya

We also should remember, when we go shopping, to get 4 items: oranges, cheese, bread, olives.
