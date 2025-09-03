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
