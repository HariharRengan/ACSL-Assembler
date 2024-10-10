# ACSL-Assembler
An assembler for the American Computer Science League's Assembly language syntax.

The assembler accepts an array containing triplets. Each element of those triplets correspond to the Label, Opcode, and Loc respectively (as outlined in the ACSL Wiki).
If there is no Label, leave the first element of the array as a blank string <code>""</code> and make all values strings (e.g. <code>"LOAD"</code> and <code>"-8"</code>)
An example input is in the <code>main.py</code> file.

ACSL Wiki: https://www.categories.acsl.org/wiki/index.php?title=Assembly_Language_Programming
