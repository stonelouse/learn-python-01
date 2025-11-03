# 8. Testing and Test-Driven Development

## 8.5 Refactor

- continued see [hartl](../README.md#hartl) p.220

- Our current code relies on a rather *cumbersome* `for` loop that appends to a list  
  … rather than creating it all at once. 
  
- In this section, we’ll **refactor** our code,  
  … which is the **process of changing the form of code without changing its function**.

- I suggest **making changes incrementally**  
  and **running the test suite after each change**  
  to confirm that the suite is **still GREEN** and there are **no regressions**.

### Applying list and generator comprehensions

- The Pythonic way of creating the list is to use [*list comprehension*](../chp006_funcprog/README.006.01.funcprog.list-comprehensions.md#62-list-comprehensions-with-conditions).

  ``` Python
  >>> content = "Madam, I'm Adam."
  >>> # List comprehension
  >>> [c for c in content]
  ['M', 'a', 'd', 'a', 'm', ',', ' ', 'I', "'", 'm', ' ', 'A', 'd', 'a', 'm', '.']
  >>> # List comprehension with condition
  >>> import re
  >>> [c for c in content if re.search(r"[a-zA-Z]", c)]
  ['M', 'a', 'd', 'a', 'm', 'I', 'm', 'A', 'd', 'a', 'm']
  >>> # `.join()` lets us replicate the current functionality of `.letters()`
  >>> "".join([c for c in content if re.search(r"[a-zA-Z]", c)])
  'MadamImAdam'
  ```

- In fact, inside the argument to `.join()`  
  … we can **omit the *square brackets*** and use a [*generator comprehension*](../chp006_funcprog/README.006.03.funcprog.generator-set-comprehensions.md#641-generator-comprehensions) instead:

  ``` Python
  >>> # …
  >>> "".join(c for c in content if re.search(r"[a-zA-Z]", c))
  'MadamImAdam'
  >>> 
  ```

- see `…/learn_python_01_package_008_tutorial/src/palindrome_stonelouse/phrase.py`  
  … commit `2b5c98f895d85c5793f1a8525f7ded619f095b75`.

  ``` Python
  # …
  def letters(self):
    """Return only the letters in the content."""
    return "".join(c for c in self.content if re.search(r"[a-zA-Z]", c))
  ```

- *Functional programs* are **harder to build up incrementally**,  
  … which is *one reason why it’s so nice to have a test suite*  
  … to check that our changes had their intended effect.

### Applying `re.findall()`

- [*Regular expressions*](https://docs.python.org/3/library/re.html) have a [`findall()`](https://docs.python.org/3/library/re.html#re.findall) method  
  … that lets us select regex-matching characters directly from a string:

  ``` Python
  >>> import re
  >>> re.findall(r"[a-zA-Z]", "Madam, I'am Adam.")
  ['M', 'a', 'd', 'a', 'm', 'I', 'a', 'm', 'A', 'd', 'a', 'm']
  >>> "".join(re.findall(r"[a-zA-Z]", "Madam, I'am Adam."))
  'MadamIamAdam'
  ```  

  So we can simplify the application code even further.

  - see `…/learn_python_01_package_008_tutorial/src/palindrome_stonelouse/phrase.py`  
  … commit `6a2779f3026f5f8e49efc36002f67de0baa61b88`.
