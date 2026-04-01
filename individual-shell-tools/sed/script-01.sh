#!/bin/bash

set -euo pipefail


$ sed -i 's/i/I/g' input.txt
roman@Zenbook:~/Migracode/Module-Tools/individual-shell-tools/sed$ cat input.txt 
ThIs Is a sample fIle for experImentIng wIth sed.

It contaIns many lInes, and there are some thIngs you may want to do wIth each of them.

We'll Include some score InformatIon:
37 AlIsha
15 Jacob
7 PIetro
3 Katya

We also should remember, when we go shoppIng, to get 4 Items: oranges,cheese,bread,olIves.

# TODO: Write a command to output input.txt with all occurrences of the letter `i` replaced with `I`.
# The output should contain 11 lines.
# The first line of the output should be: "ThIs Is a sample fIle for experImentIng wIth sed.".
