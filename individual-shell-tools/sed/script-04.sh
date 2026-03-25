#!/bin/bash

set -euo pipefail

# TODO: Write a command to output input.txt replacing every occurrence of the string "We'll" with "We will".
# The output should contain 11 lines.

$ sed -i "s/We'll/We will/g" input.txt
$ cat input.txt 
This is a sample file for experimenting with sed.

it contains many lines, and there are some things you may want to do with each of them.

We will include some score information:
37 Alisha
15 Jacob
7 Pietro
3 Katya

We also should remember, when we go shopping, to get 4 items: oranges,cheese,bread,olives.