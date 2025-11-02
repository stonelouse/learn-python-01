# 8. Testing and Test-Driven Development

## 8.4 Green

- continued see [hartl](../README.md#hartl) p.214

- Now that we have *RED* tests to capture the enhanced behavior of our palindrome detector, it’s time to make them *GREEN*.

- Part of the philosophy of TDD is to get them passing  
  … **without worrying too much at first about the quality** of the implementation.

- For the first approach, we are using a *regexp*

  ``` Python
  >>> import re
  >>> re.search(r"[a-zA-Z]","M")
  <re.Match object; span=(0, 1), match='M'>
  >>> bool(re.search(r"[a-zA-Z]","M"))
  True
  >>> bool(re.search(r"[a-zA-Z]","m"))
  True
  >>> bool(re.search(r"[a-zA-Z]"," "))
  False
  >>> bool(re.search(r"[a-zA-Z]",","))
  False  

  >>> content = "Madam, I'm Adam."
  >>> the_letters = []
  >>> for char in content:
  ...   if re.search(r"[a-zA-Z]", char):
  ...     the_letters.append(char)
  ... 
  >>> "".join(the_letters)
  'MadamImAdam'  
  ```

- see `…/learn_python_01_package_008_tutorial/src/palindrome_stonelouse/phrase.py` commit `403d0b64bedaa30ed98e013fa2db5d7c1ec0d75c` for the first *GREEN* version of `Phrase` class.
