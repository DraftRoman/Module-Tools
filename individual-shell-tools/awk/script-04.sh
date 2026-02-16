#!/bin/bash

set -euo pipefail

# Output the names of each player in London along with the score from their last attempt.
# For lines with fewer than 5 columns, print the last column.
awk '{if (NF >= 5 && $2 == "London") print $1, $5; else if (NF < 5 && $2 == "London") print $1, $NF}' scores-table.txt
