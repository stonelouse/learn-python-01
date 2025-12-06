# Return the paragraphs from a Wikipedia link, stripped of reference numbers.
# Especially useful for text-to-speech (both native and foreign).
# Example:
# PS …\learn-python-01> python .\chp009_shell_scripts\wiki_text_extractor.py "https://en.wikipedia.org/wiki/Python_(programming_language)"
# user@linux:…/__learn-python-01/chp009_shell_scripts> python3 ./wiki_text_extractor.py "https://en.wikipedia.org/wiki/Python_(programming_language)"
import sys
import requests
from bs4 import BeautifulSoup


def print_paragraphs(doc, out_file=None):
    if out_file:
        with open(out_file, "w", encoding="utf-8") as f_out:
            for paragraph in doc("p"):
                f_out.write(
                    paragraph.text
                )  # line breaks are already contained in paragraph.text
    else:
        for paragraph in doc("p"):
            print(paragraph.text)


def main():
    url = sys.argv[1]

    print(f"Process URL='{url}'")

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    content = requests.get(url, headers=headers).content.decode("utf-8")

    # for line in content.splitlines(): # TODO debugging
    #     print(line)

    # Create a Beautiful Soup document from live URL.
    doc = BeautifulSoup(content, features="html.parser")

    print_paragraphs(doc, out_file="wiki_paragraphs_with_references.txt")

    # Remove references from wiki document.
    for ref in doc("sup", class_="reference"):
        ref.decompose()

    print_paragraphs(doc, out_file="wiki_paragraphs_without_references.txt")


if __name__ == "__main__":
    main()
