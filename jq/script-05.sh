#!/bin/bash

set -euo pipefail

# The input for this script is the scores.json file.
# TODO: Write a command to output the names of each player, as well as their city.
# Your output should contain 6 lines, each with two words on it.
jq -r '.[] | [.name, .city] | join(", ")' scores.json  
# .[] goes through each object   [.name, .city] = creates a temporary array for name and city  and then we use join to join name and city
