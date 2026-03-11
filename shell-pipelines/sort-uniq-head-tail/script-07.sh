#!/bin/bash

set -euo pipefail

# The input for this script is the events-with-timestamps.txt file.
# TODO: Write a command to show how many times anyone has entered and exited.
# It should be clear from your script's output that there have been 5 Entry events and 4 Exit events.
# The word "Event" should not appear in your script's output.

# Count entries per person
echo "Entry counts per person:"
grep 'Entry' events-with-timestamps.txt | awk '{print $4}' | sort | uniq -c

# Count exits per person
echo "Exit counts per person:"
grep 'Exit' events-with-timestamps.txt | awk '{print $4}' | sort | uniq -c

# Show total number of entries
echo "Total Entry: $(grep -w 'Entry' events-with-timestamps.txt | wc -l)"

# Show total number of exits
echo "Total Exit:  $(grep -w 'Exit' events-with-timestamps.txt | wc -l)"


