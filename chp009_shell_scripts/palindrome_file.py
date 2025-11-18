#!/usr/bin/env python3

# When we want to execute this Python script in a wsl shell,
# … its necessary to store the file with LF line endings.
#
# Example
# rus@DE-FWNWTT3:/mnt/d/NoScan/home.rus/dev.ext.prj/learn-python-01/chp009_shell_scripts$ ./palindrome_file.py

import re

class Phrase:
    """A class to represent phrases."""

    def __init__(self, content):
        self.content = content

    def ispalindrome(self):
        """Return True for a palindrome, False otherwise."""
        return self._processed_content() == reverse(self._processed_content())

    def _processed_content(self):
        """Process content for palindrome testing."""
        """Process content for palindrome testing."""
        return self.letters_and_digits().lower()

    def letters_and_digits(self):
        """Return only the letters in the content."""
        return "".join(re.findall(r"[A-Za-z0-9]", self.content))

    def __iter__(self):
        self.phrase_iterator = iter(self.content)
        return self

    def __next__(self):
        return next(self.phrase_iterator)


def reverse(string):
    """Reverse a string."""
    return "".join(reversed(string))

print("hello, world!")

with open("my_phrases.txt") as file:
    text = file.read()
    for line in text.splitlines(): # Arguably not Pythonic!
        if Phrase(line).ispalindrome():
            print(f"palindrome detected: {line}")
