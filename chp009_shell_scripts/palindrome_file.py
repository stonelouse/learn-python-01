#!/usr/bin/env python3

# When we want to execute this Python script in a wsl shell,
# … its necessary to store the file with LF line endings.

from palindrome_stonelouse.phrase import Phrase

with open("phrases.txt") as file:
    text = file.read()
    for line in text.splitlines():  # Arguably not Pythonic!
        if Phrase(line).ispalindrome():
            print(f"palindrome detected: {line}")
