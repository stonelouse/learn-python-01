# 3. Lists

- [3. Lists](#3-lists)
  - [3.1 Splitting](#31-splitting)
    - [`split()` method](#split-method)
    - [`splitlines()` method](#splitlines-method)
    - [`list()` function](#list-function)

- see [hartl](../README.md#hartl) p.69

- **Lists** is the *data type*, which is the **general Python container**  
  … for a list of arbitrary *elements* in **particular order**.

- Python's *Lists* are similar to the *array* data type in other languages.  
  
- GitHub Copilot:  
  > Python **does not have** a *built-in data type called 'array'*  
  > in the same way as some other languages like Java or C.
  >
  > Instead, Python provides:  
  > - The `list` type,  
  >   … which is a flexible, *built-in sequence type*  
  >   … that can store elements of *any type*  
  >   … and is *used like an array* in many cases.
  > - The *`array` module*,  
  >   … which provides an `array` type (`array.array`)  
  >   … for storing *elements of a single numeric* type **more efficiently**,  
  >   … but it is not as commonly used as lists.
  > - For advanced *numerical arrays*, the *NumPy* library (not built-in)  
  >   … provides the `ndarray` type,  
  >   … which is widely used in scientific computing.  
  >
  > In summary:  
  > … Python’s closest built-in equivalent to an array is the *list type*.

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
