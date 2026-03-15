#!/bin/bash

set -euo pipefail

# The input for this script is the scores.json file.
# TODO: Write a command to output just the names of each player along with the number of times they've played the game.
# Your output should contain 6 lines, each with one word and one number on it.
# The first line should be "Ahmed 3" with no quotes.

# [{"name": "Ahmed", "city": "London", "scores": [1, 10, 4]}, {"name": "Basia", "city": "London", "scores": [22, 9, 6]}, {"name": "Mehmet", "city": "Birmingham", "scores": [3, 12, 17]}, {"name": "Leila", "city": "London", "scores": [1]}, {"name": "Piotr", "city": "Glasgow", "scores": [15, 2, 25, 11, 8]}, {"name": "Chandra", "city": "Birmingham", "scores": [12, 6]}]

jq -r '.[] | .name + " " + (.scores | length | tostring)' scores.json