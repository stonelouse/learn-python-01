# 5. Functions and Iterators

- Todo

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

  ``` pwsh
  (venv) PS D:\home.UserRus\Documents.Notes\__learn-python-01\chp005_functions_iterators> python .\p005.02.is_palindrome.py
  'kayak' is a palindrome: True
  'foobar' is a palindrome: False
  'racecar' is a palindrome: True
  'Racecar' is a palindrome: False
  '' is a palindrome: True
  ```
