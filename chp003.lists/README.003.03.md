# 3. Lists

- [3. Lists](#3-lists)
  - [3.5 List Iteration](#35-list-iteration)
    - [Indirectly iteration with the `for loop` and *index*](#indirectly-iteration-with-the-for-loop-and-index)
    - [Directly iteration with the `for loop`](#directly-iteration-with-the-for-loop)
    - [`enumerate()` function](#enumerate-function)
    - [`break` keyword](#break-keyword)
    - [`repr()` function](#repr-function)

## 3.5 List Iteration

- continued see [hartl](../README.md#hartl) p.83

### Indirectly iteration with the `for loop` and *index*

- One of the most common tasks with lists is **iterating** through their elements and  
  … performing an *operation* with *each one*.

  ``` Python
  >>> phrase = ["To", "be", "or", "not", "to", "be"]
  >>> for i in range(len(phrase)): # ☝ NOT Pythonic
  ...     print(phrase[i])
  ...     
  To  
  be  
  or  
  not 
  to  
  be 
  ```

- That's convenient, but is not the *pythonic* way to iterate through lists.  

### Directly iteration with the `for loop`

- Using the following style of `for` loop, we can iterate directly through the elements in a list.
  
  ``` Python
  >>> for p in phrase: # Pythonic
  ...     print(p)
  ...     
  To
  be
  or
  not
  to
  be
  ```  

### `enumerate()` function

- The built-in function [`enumerate()`](https://docs.python.org/3/library/functions.html#enumerate) provides an *enumerate object* with the *element* and its *index*:

  ``` Python
  >>> list(enumerate(phrase))
  [(0, 'To'), (1, 'be'), (2, 'or'), (3, 'not'), (4, 'to'), (5, 'be')]
  >>>
  >>> for i, p in enumerate(phrase):
  ...     print(f"p[{i}]: {p}")
  ... 
  p[0]: To
  p[1]: be
  p[2]: or
  p[3]: not
  p[4]: to
  p[5]: be
  ```

### `break` keyword

- The `break` keyword allows to *break out* of a loop early:

  ``` Python
  >>> for i, p in enumerate(phrase):
  ...     if i == 4:
  ...         print("... enough")
  ...         break
  ...     else:
  ...         print(f"p[{i}]: {p}")
  ... 
  p[0]: To
  p[1]: be
  p[2]: or
  p[3]: not
  ... enough
  ```

### `repr()` function

- Exercise 3.5.1

  ``` Python
  >>> phrase = ["To", "be", "or", "not", "to", "be"]
  >>> esarhp = reversed(phrase)
  >>> esarhp
  <list_reverseiterator object at 0x000002B7E30199C0>
  >>> esarhp = list(reversed(phrase))
  >>> esarhp
  ['be', 'to', 'not', 'or', 'be', 'To']
  ```

- The built-in function [`repr()`](https://docs.python.org/3/library/functions.html#repr) return a string containing a *printable representation* of an *object*

  ``` Python
  >>> a = ["ant", "bat", "cat", 42]
  >>> for i, e in enumerate(a):
  ...     print(f"e[{i}]: {e}")
  ... 
  e[0]: ant
  e[1]: bat
  e[2]: cat
  e[3]: 42
  >>> for i, e in enumerate(a):
  ...     print(f"e[{i}]: {repr(e)}")
  ... 
  e[0]: 'ant' # string representation
  e[1]: 'bat'
  e[2]: 'cat'
  e[3]: 42
  ```
