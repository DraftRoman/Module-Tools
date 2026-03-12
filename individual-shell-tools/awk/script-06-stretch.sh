#!/bin/bash

set -euo pipefail

# NOTE: This is a stretch exercise - it is optional.

# TODO: Write a command to output the total of adding together all players' first scores.
# Your output should be exactly the number 54.
awk '{
  for(i=3;i<=3;i++) total += $i
} END {print total}' scores-table.txt