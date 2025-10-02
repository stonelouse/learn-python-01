# 5. Functions and Iterators

- [5. Functions and Iterators](#5-functions-and-iterators)
  - [5.3.1 Generators](#531-generators)

## 5.3.1 Generators

- continued see [hartl](../README.md#hartl) p.143

- A **generator** is a *special kind of iterator* built  
  … using a special operation called [`yield()`](https://docs.python.org/3/reference/datamodel.html#generator-functions).

- We can *iterate* over the *the generator object*:

  ``` Python
  >> def characters(string):
  ...     for c in string:
  ...             yield c
  ...     return None
  ...
  >>> type(characters)
  <class 'function'>
  >>> for c in characters("foobar"):
  ...     print(c)
  ...
  f
  o
  o
  b
  a
  r
  ```

  … but it is not very useful since we can already iterate over regular strings:
  
  ``` Python
  >>> for c in "foobar":
  ...     print(c)
  ... 
  f
  o
  o
  b
  a
  r
  ```

- We can *join* the *generator object* as well:

  ``` Python
  >>> "".join(characters("foobar"))
  'foobar'
  ```

- Example: Function to check if a number contains all digits `0-9`

  ``` Python
  # We appy the following concept
  >>> set("123123123") == set("321231132")
  True
  >>> def first_has_all_digits(numbers):
    ...   for n in numbers:
  ...     if set(str(n)) == set("0123456789"):
  ...       return n
  ...   return None
  ... 
  >>> first_has_all_digits(["1230567890", "0123455789", "0129874563"])
  '0129874563'
  ```

  Now we create a **square generator** …

  ``` Python
  >>> def squares_generator():
  ...   # we have left off the `return None` because it is the default
  ...   for n in range(10**8 + 1):
  ...     yield n**2 
  ```

  … which supplies the next square **only when needed**!

  ``` Python
  >>> first_has_all_digits(squares_generator())
  1026753849
  ```

  By the way as of Python 3, the `range()` function also produces the next element in the range only when needed.

- Exercies 5.3.2.2

  ``` Python
  >> string = "racecar"
  >>> is_palindrome(string)
  True
  >>> string.lower() == string.lower()[::-1]
  True
  >>> string = "foobar"
  >>> is_palindrome(string)
  False
  >>> string.lower() == string.lower()[::-1]
  False
  ```

- Exercies 5.3.2.3

  ``` Python
  >> string = "racecar"
  >>> is_palindrome(string)
  True
  >>> string.lower() == string.lower()[::-1]
  True
  >>> string = "foobar"
  >>> is_palindrome(string)
  False
  >>> string.lower() == string.lower()[::-1]
  False
  ```
