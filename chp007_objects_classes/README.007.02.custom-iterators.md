# 7. Objects and Classes

- [7. Objects and Classes](#7-objects-and-classes)
  - [7.2 Custom Iterators](#72-custom-iterators)

## 7.2 Custom Iterators

- continued see [hartl](../README.md#hartl) p.176

- In this section we'll learn how to add an iterator to a custom class.

- The general requirements for an iterator are twofold:

  1. An [**`__iter__`**](https://docs.python.org/3/library/stdtypes.html#iterator.__iter__) method  
     … that does any necessary setup and then returns `self`
  2. A [**`__next__`**](https://docs.python.org/3/library/stdtypes.html#iterator.__next__) method that returns the *next element in the sequence*

  ``` Python
  >>> string_iterator = iter("foo")
  >>> type(string_iterator)
  <class 'str_ascii_iterator'>  
  >>> next(string_iterator)
  'f'
  >>> next(string_iterator)
  'o'
  >>> next(string_iterator)
  'o'
  # `StopIteration` exception was thrown
  >>> next(string_iterator)
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
      import platform
  StopIteration
  >>>
  ```

- Note that, as with `__init__`, the methods to perform iteration use the **double-underscore convention** to indicate that they are *magic methods* used to **define the behavior of Python objects**.

- With this we implement the *iterator*

  see `chp007_objects_classes\package\palindrome.py`  
  commit `3d5b48d4425f96ef96e7b1d7beda1a5c453bc13d`

   ``` Python
  >>> import palindrome
  >>> phrase = palindrome.Phrase("Mom")
  >>> phrase.ispalindrome()
  True
  >>> for c in phrase:
  ...   print(c)
  ... 
  M
  o
  m
  >>> phrase_iterator = iter(phrase)
  >>> next(phrase_iterator)
  'M'   
  ```

- Exercise 7.2.1

  ``` Python
  >>> list(phrase)
  ['M', 'o', 'm']
  >>> "-".join(phrase)
  'M-o-m'
  ```
