#!/bin/bash

set -euo pipefail

# TODO: Write a command to output input.txt removing any line which contains a number.
# The output should contain 6 lines.
#grep -v '[0-9]' input.txt
sed '/[0-9]/d' input.txt
