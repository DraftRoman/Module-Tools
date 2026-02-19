#!/bin/bash

set -euo pipefail

# NOTE: This is a stretch exercise - it is optional.

# TODO: Write a command to output the total of adding together all players' first scores.
# Your output should be exactly the number 54.

awk '{s += $3} END {print s}' scores-table.txt

# {s += $3}; (action)
# END {print s}' (at the end, print the sum!)