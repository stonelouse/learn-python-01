#!/usr/bin/env python3

import requests
from palindrome_stonelouse.phrase import Phrase


def main():
    url = "https://cdn.learnenough.com/phrases.txt"

    response = requests.get(url)
    palindromes = [
        line
        for line in response.content.decode("utf-8").splitlines(keepends=True)
        if Phrase(line).ispalindrome()
    ]

    with open("palindromes_from_url.txt", "w") as pfile:
        for p in palindromes:
            pfile.write(p)
            # Note: 'p' already includes its own newline character


if __name__ == "__main__":
    main()
