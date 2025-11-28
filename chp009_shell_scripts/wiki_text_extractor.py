# Return the paragraphs from a Wikipedia link, stripped of reference numbers.
# Especially useful for text-to-speech (both native and foreign).
# Example:
# PS …\learn-python-01> python .\chp009_shell_scripts\wiki_text_extractor.py  https://es.wikipedia.org/wiki/Python
import sys

url = sys.argv[1]

print(f"Process URL='{url}'")
