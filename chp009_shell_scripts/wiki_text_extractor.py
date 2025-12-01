# Return the paragraphs from a Wikipedia link, stripped of reference numbers.
# Especially useful for text-to-speech (both native and foreign).
# Example:
# PS …\learn-python-01> python .\chp009_shell_scripts\wiki_text_extractor.py  https://es.wikipedia.org/wiki/Python
import sys
import requests
from bs4 import BeautifulSoup

url = sys.argv[1]

print(f"Process URL='{url}'")

content = requests.get(url).content.decode("utf-8")

# for line in content.splitlines(): # TODO debugging
#     print(line)

# Create a Beautiful Soup document from live URL.
doc = BeautifulSoup(content, features="html.parser")

# Remove references from wiki document.
for ref in doc("sup", class_="reference"):
    ref.decompose()

for paragraph in doc("p"):
    print(paragraph.text)
