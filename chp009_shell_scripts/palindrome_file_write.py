#!/usr/bin/env python3

from palindrome_stonelouse.phrase import Phrase

with open("phrases.txt") as file:
    palindromes = [line for line in file.readlines() 
                    if Phrase(line).ispalindrome()]

with open("palindromes.txt", "w") as pfile:
    for p in palindromes:
        pfile.write(p)
        # Note: 'p' already includes its own newline character
