# 5. Functions and Iterators

- [5. Functions and Iterators](#5-functions-and-iterators)
  - [5.3 Iterators](#53-iterators)
    - [Iterate over *iterators* with `for` loop](#iterate-over-iterators-with-for-loop)
    - [Creating *lists* with `list()` from *iterators*](#creating-lists-with-list-from-iterators)
    - [Using `chp005_functions_iterators\package\p005_02_is_palindrome.py` in the REPL](#using-chp005_functions_iteratorspackagep005_02_is_palindromepy-in-the-repl)
      - [Alt.1: Import as Module](#alt1-import-as-module)
      - [Alt.2: Import the function directly and reload module if function implementation changed](#alt2-import-the-function-directly-and-reload-module-if-function-implementation-changed)

## 5.3 Iterators

- continued see [hartl](../README.md#hartl) p.139

- First version of a `is_palindrome()` *fn*

  ``` Python
  >>> def is_palindrome(value):
  ...     elements = list(value)
  ...     elements.reverse()
  ...     reversed = "".join(elements)
  ...     return reversed == value
  ...     
  >>> is_palindrome("kajak")
  True
  >>> is_palindrome("foobar")
  False
  >>> is_palindrome("")
  True
  ```

- *Strings* do not have a `.reversed()` method, but you can use the built-in [`reversed()`](https://docs.python.org/3/library/functions.html#reversed) function on a string. This returns an **iterator** that yields the *characters* of the string in *reverse order*. This *iterator* can be directly passed to the *string's* [`.join()`](https://docs.python.org/3/library/stdtypes.html#str.join) method.

  ``` Python
  >>> "foobar".reverse()
  Traceback (most recent call last):
    File "<python-input-4>", line 1, in <module>
      "foobar".reverse()
      ^^^^^^^^^^^^^^^^
  AttributeError: 'str' object has no attribute 'reverse'

  >>> reversed("foobar")
  <reversed object at 0x0000020064371750>

  >>> "".join(reversed("foobar"))
  'raboof'
  ```

- An [**Iterator**](https://docs.python.org/3/library/stdtypes.html#iterator-types) represents a **stream of data**.  
  … In the case above, it represents a stream of *characters* that get *accessed in sequence*.

### Iterate over *iterators* with `for` loop

- One way to iterate through an *iterator* is to apply a `for` loop

  ``` Python
  >>> for c in reversed("foobar"):
  ...     print(c)
  ... 
  r
  a
  b
  o
  o
  f
  ```

### Creating *lists* with `list()` from *iterators*

- [`list()`](https://docs.python.org/3/library/functions.html#func-list) applied to *iterators*

  ``` Python
  >>> list(reversed("foobar"))
  ['r', 'a', 'b', 'o', 'o', 'f']
  ```

- Next version: Providing a function in a separate file  
  … see `chp005_functions_iterators\package\p005_02_is_palindrome.py`  
  … and calling that function from `chp005_functions_iterators\p005.02.is_palindrome.py`

  ``` pwsh
  (venv) PS D:\home.UserRus\Documents.Notes\__learn-python-01\chp005_functions_iterators> python .\p005.02.is_palindrome.py
  'kayak' is a palindrome: True
  'foobar' is a palindrome: False
  'racecar' is a palindrome: True
  'Racecar' is a palindrome: False
  '' is a palindrome: True
  ```

### Using `chp005_functions_iterators\package\p005_02_is_palindrome.py` in the REPL

#### Alt.1: Import as Module

- This section was developed with assistance from *GitHub Copilot*.

- We *import* `p005_02_is_palindrome.py` as a *module*.  
  … Using [`importlib.reload()`](https://docs.python.org/3/library/importlib.html#importlib.reload), we can reload the it after a code change.

  ``` Python
  >>> import importlib
  >>> import chp005_functions_iterators.package.p005_02_is_palindrome as pal_module
  >>> pal_module.is_palindrome("otto")
  True
  >>> pal_module.is_palindrome("Otto")
  False
  >>> # Now, the implementation from `is_palindrome()` was changed amd is case-insensitive.
  >>> pal_module.is_palindrome("Otto")
  False # … ☝ Note: nothing changed!
  >>> importlib.reload(pal_module)
  <module 'chp005_functions_iterators.package.p005_02_is_palindrome' from 'D:\\home.UserRus\\Documents.Notes\\__learn-python-01\\chp005_functions_iterators\\package\\p005_02_is_palindrome.py'>
  >>> pal_module.is_palindrome("Otto")
  True # ☝ Note: now it changed!
  ```

#### Alt.2: Import the function directly and reload module if function implementation changed

- This section was developed with assistance from *GitHub Copilot*.

- We *import* both,  
  … `p005_02_is_palindrome.py` as a *module*, and  
  … the *function* `is_palindrome()` additionally.

  If the implementation of `is_palindrome()` was changed, wie **reload** the *module* and re-**import** the *function* again:

  ``` Python
  >>> is_palindrome("Otto") # `is_palindrome()` is unknown
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
      import platform
      ^^^^^^^^^^^^^
  NameError: name 'is_palindrome' is not defined
  >>> from chp005_functions_iterators.package import p005_02_is_palindrome
  >>> from chp005_functions_iterators.package.p005_02_is_palindrome import is_palindrome
  >>> is_palindrome("Otto")
  False
  >>> # Now, the implementation from `is_palindrome()` was changed amd is case-insensitive.
  >>> is_palindrome("Otto")
  False # … ☝ Note: nothing changed!
  >>> import importlib
  >>> importlib.reload(p005_02_is_palindrome)
  <module 'chp005_functions_iterators.package.p005_02_is_palindrome' from 'D:\\home.UserRus\\Documents.Notes\\__learn-python-01\\chp005_functions_iterators\\package\\p005_02_is_palindrome.py'>
  >>> is_palindrome("Otto")
  False # … ☝ Note: still no change!
  >>> from chp005_functions_iterators.package.p005_02_is_palindrome import is_palindrome
  >>> is_palindrome("Otto")
  True # … ☝ Note: now it changed!
  ```
