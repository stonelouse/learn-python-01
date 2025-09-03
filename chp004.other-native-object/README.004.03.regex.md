# 4. Other Native Objects

- TODO

## 4.3 Regular Expressions - *regex*

- continued see [hartl](../README.md#hartl) p.103

### Creating a *regex*

- We can create a new regex using a *string*,  
  … which is nearly always a [raw string](../chp002.strings/README.002.01.md#raw-strings)  
  … so that it handles special characters like backslashes automatically.

  ``` Python
  >>> zip_code = r"\d{5}" # a raw string
  ```

### `re` module

- `re` module provides a `search()` function which is useful in a boolean context

  ``` Python
  # …
  >>> zip_code = r"\d{5}" # a raw string
  >>> import re
  >>> re.search(zip_code, "Beverly Hills 90210")
  <re.Match object; span=(14, 19), match='90210'>
  >>> if re.search(zip_code, "Beverly Hills 90210"):
  ...     print("It's got a ZIP code")
  ... else:
  ...     print("no match")
  ...     
  It's got a ZIP code
  >>>
  ```

- Finding all string matches with `re.findall()`

  ``` Python
  >>> s = "Beverly Hills 90210 was a '90s TV show set in Los Angeles. 91125 is another ZIP code in the Los Angeles' area"
  >>> s
  "Beverly Hills 90210 was a '90s TV show set in Los Angeles. 91125 is another ZIP code in the Los Angeles area"
  >>> import re
  >>> re.findall(zip_code, s)
  ['90210', '91125']

  # Finding all multi-letter words that are ALL CAPS
  >>> re.findall(r"[A-Z]{2,}", s)
  ['TV', 'ZIP']
  ```

- Splitting with `re.split()` *fn*

  ``` Python
  >>> "ant bat cat duck".split(" ")
  ['ant', 'bat', 'cat', 'duck']
  >>> "ant bat  cat   duck".split(" ")
  ['ant', 'bat', '', 'cat', '', '', 'duck']
  >>> import re
  >>> re.split(r"\s+", "ant bat  cat   duck")
  ['ant', 'bat', 'cat', 'duck']
  # By default, .split() called without argument splits on whitespace automatically
  >>> "ant bat  cat   duck".split()
  ['ant', 'bat', 'cat', 'duck']
  >>> "ant bat  cat\tduck".split()
  ['ant', 'bat', 'cat', 'duck']
  ```

- Exercise 4.3.2

  ``` Python
  >>> # exercise 4.3.2.1
  >>> zip_extended = r"\d{5}-\d{4}"
  >>> import re
  >>> re.search(zip_extended, "10118-0110")
  <re.Match object; span=(0, 10), match='10118-0110'>
  >>> re.search(zip_extended, "10118_0110")
  >>> re.search(zip_extended, "10118_0110") == None
  True
  >>> re.search(zip_extended, "10118-110") == None
  True
  >>> re.search(zip_extended, "1011-0110") == None
  True
  >>> re.search(zip_extended, "1011-01109") == None
  True
  >>> re.search(zip_extended, "10119-0110") == None
  False
  >>> re.search(zip_extended, "a0119-0110") == None
  True
  >>> re.search(zip_extended, "10119-011b") == None
  True
  ```

  ``` Python
  >>> # exercise 4.3.2.2
  >>> poem = """Let me not to the marriage of true minds
  ... Admit impediments. Love is not love
  ... Which alters when it alteration finds,
  ... Or bends with the remover to remove.
  ... O no, it is an ever-fixed mark
  ... That looks on tempests and is never shaken
  ... It is the star to every wand'ring bark,
  ... Whose worth's unknown, although his height be taken.
  ... Love's not time's fool, though rosy lips and cheeks
  ... Within his bending sickle's compass come:
  ... Love alters not with his brief hours and weeks,
  ... But bears it out even to the edge of doom.
  ...     If this be error and upon me proved,
  ...     I never writ, nor no man ever loved."""
  >>> re.split(r"\n", poem)
  ['Let me not to the marriage of true minds', 'Admit impediments. Love is not love', 'Which alters when it alteration finds,', 'Or bends with the remover to remove.', 'O no, it is an ever-fixed mark', 'That looks on tempests and is never shaken', "It is the star to every wand'ring bark,", "Whose worth's unknown, although his height be taken.", "Love's not time's fool, though rosy lips and cheeks", "Within his bending sickle's compass come:", 'Love alters not with his brief hours and weeks,', 'But bears it out even to the edge of doom.', '    If this be error and upon me proved,', '    I never writ, nor no man ever loved.']
  >>> len(re.split(r"\n", poem)) == 14
  True
  >>>
  ```
