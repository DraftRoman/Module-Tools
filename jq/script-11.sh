#!/bin/bash

set -euo pipefail

# The input for this script is the scores.json file.
# TODO: Write a command to output the total of adding together all scores from all games from all players.
# Your output should be exactly the number 164.

# [{"name": "Ahmed", "city": "London", "scores": [1, 10, 4]}, {"name": "Basia", "city": "London", "scores": [22, 9, 6]}, {"name": "Mehmet", "city": "Birmingham", "scores": [3, 12, 17]}, {"name": "Leila", "city": "London", "scores": [1]}, {"name": "Piotr", "city": "Glasgow", "scores": [15, 2, 25, 11, 8]}, {"name": "Chandra", "city": "Birmingham", "scores": [12, 6]}]

# jq -r '.[] | .scores[0] | add' scores.json nned nums in array
jq -r '[.[] | .scores[]] | add' scores.json
