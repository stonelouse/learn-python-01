# 3. Lists

- [3. Lists](#3-lists)
  - [3.1 Splitting](#31-splitting)
    - [`split()` method](#split-method)
    - [`splitlines()` method](#splitlines-method)
    - [`list()` function](#list-function)
  - [3.2 List Access](#32-list-access)
    - [Literal square bracket syntax](#literal-square-bracket-syntax)
    - [List access - bracket notation](#list-access---bracket-notation)
    - [Lists in a Boolean context](#lists-in-a-boolean-context)

## 3.1 Splitting

### `split()` method

- see [hartl](../README.md#hartl) p.69

- We can split a string with the [`str.split()`](https://docs.python.org/3.3/library/stdtypes.html#str.split) method in a `list` of words

  ``` Python
  >>> "ant,bat,cat".split(",")
  ['ant', 'bat', 'cat']
  >>> "ant bat cat".split(" ")
  ['ant', 'bat', 'cat']
  >>> len("ant bat cat".split(" "))
  3   
  >> "To be\nor not\tto be".split() # default (no args) split on whitespace
  ['To', 'be', 'or', 'not', 'to', 'be']  
  ```

### `splitlines()` method

- Convenience method [`str.splitlines()`](https://docs.python.org/3.3/library/stdtypes.html#str.splitlines) for splitting strings with multiple lines

  ``` Python
  >>> s = """
  ... This is line 1
  ... This is line 2
  ... This is line 3
  ... """
  >>> s.split("\n")
  ['', 'This is line 1', 'This is line 2', 'This is line 3', '']
  >>> s.splitlines()
  ['', 'This is line 1', 'This is line 2', 'This is line 3']
  >>> s.splitlines(True)
  ['\n', 'This is line 1\n', 'This is line 2\n', 'This is line 3\n']  
  ```  

### `list()` function

- Github Copilot:  
  
  > `list()` in Python acts like a constructor for the built-in `list` class.  
  >
  > When you call `list()`, it creates a new, empty list object.
  >
  > You can also pass an iterable (like a string, tuple, or another list) to `list()` to create a new list containing the elements of that iterable. So, `list()` is the standard way to construct a new list in Python.

- Using [`list()` function](https://docs.python.org/3/library/functions.html#func-list) to create a list from a string

  ``` Python
  >>> # splitting a string into a list of characters
  >>> "badger".split("") # doesn't work
  Traceback (most recent call last):
    File "<python-input-7>", line 1, in <module>
      "badger".split("") # doesn't work
      ~~~~~~~~~~~~~~^^^^
  ValueError: empty separator
  >>> list("badger") # use list() function for this
  ['b', 'a', 'd', 'g', 'e', 'r']
  ```

- Because Python can naturally *iterate* over a string's characters, this technique is rarely needed explicitly; instead we'll typical use *iterators*.

- Exercise 3.1.1

  ``` Python
  >>> a = "A man, a plan, a canal, Panama".split(", ") # should create a list with 4 words
  >>> a
  ['A man', 'a plan', 'a canal', 'Panama']
  >>> a[::-1] # reverse the list via slice operator
  ['Panama', 'a canal', 'a plan', 'A man']
  ```

## 3.2 List Access

- see [hartl](../README.md#hartl) p.71

### Literal square bracket syntax

- Literal square bracket syntax:

  ``` Python
  >>> # creating a list using literal square-bracket syntax
  >>> a = ["badger", 42, "or not" in "To be or not to be"]
  ```

### List access - bracket notation

- List access - bracket notation

  ``` Python
  >>> # accessing list elements with `bracket notation`
  >>> a[0]
  'badger'
  >>> a[2]
  True
  >>> a[1]
  42  
  >>> a[3]
  Traceback (most recent call last):
    File "<python-input-4>", line 1, in <module>
      a[3]
      ~^^^
  IndexError: list index out of range
  >>> a[-1]
  True
  >>> a[-2]
  42
  >>> a[-3]
  'badger'
  >>> a[-4]
  Traceback (most recent call last):
    File "<python-input-8>", line 1, in <module>
      a[-4]
      ~^^^^
  IndexError: list index out of range

### Apply `len()` function on lists

- Apply `len()` function on lists

  ``` Python
  >>> len(a)
  3
  ```

### Lists in a Boolean context

- Apply `len()` function on lists

  ``` Python
  >>> bool([]) # empty list are False in a boolean context
  False
  >>> bool([1, 2, 3])
  True
  ```

- Exercise 3.2.1

  ``` Python
  >>> list(range(4))
  [0, 1, 2, 3]
  >>> list(range(5))
  [0, 1, 2, 3, 4]
  >>> list(range(17, 42))
  [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]  
  ```
