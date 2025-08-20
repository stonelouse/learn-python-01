# 2. String basics

- [2. String basics](#2-string-basics)
  - [2.3 Printing](#23-printing)
    - [`print()` – `repr()` – `None`](#print--repr--none)
    - [`print's` keyword argument `end`](#prints-keyword-argument-end)
    - [`print()` and multiple arguments](#print-and-multiple-arguments)
  - [2.4 Length, Boolean, and Control Flow](#24-length-boolean-and-control-flow)
    - [`len()`](#len)
    - [`if`](#if)
    - [`else`](#else)
    - [`elif` - "else if"](#elif---else-if)
    - [Combining and inverting booleans - `and`, `or`, `not`](#combining-and-inverting-booleans---and-or-not)
    - [Bang equals `!=`](#bang-equals-)

## 2.3 Printing

- continued see [hartl](../README.md#hartl) p.44

### `print()` – `repr()` – `None`

- operates as a **side effect**  
  … which refers to *anything a function does* **other than returning a value**.

- Indeed, print() returns a literal Python object `None`
  
  ``` Python
  >>> printResult = print('Jane Doe')
  Jane Doe
  >>> printResult
  # `print()` converts the object `None` to a string representation
  # and prints the result
  >>> print(printResult)
  None
  # we can use `repr()` (representation) to directly get the string representation
  # `repr()` works essentially with any Python object
  >>> repr(printResult)
  'None'
  >>> repr(None)
  'None'
  ```

### `print's` keyword argument `end`

- represents the character used to end of the string.  
  … default `end` is *newline* `\n`

  ``` Python
  >>> print('Jane Doe', end='\n\n')
  Jane Doe

  >>>
  >>> print("npm i", end=" && "); \
  ... print("tc")
  npm i && tc
  >>> print("foo", end=""); \
  ... print("bar", end=""); \
  ... print("baz")
  foobarbaz
  ```

### `print()` and multiple arguments

- Pass multiple arguments to `print()`
  
  ``` Python
  >>> print("foo", "bar", "baz")
  foo bar baz
  ```

## 2.4 Length, Boolean, and Control Flow

- continued see [hartl](../README.md#hartl) p.46

### `len()`

- **Built-in function**, which returns the *length* of its argument.

  ``` Python
  >>> greetings = 'Hello world'
  >>> len(greetings)
  11
  >>> len(greetings) == 11
  True
  ```

### `if`

- Block structure is indicated by **indentation**

  ``` Python
  >>> password = 'john'
  >>> if len(password) < 20: # Pythonic
  ...     print("Password is too short")
  ...     
  Password is too short
  ```

### `else`

- Control flow with `if` and `else`

  ``` Python
  >>> password = "1234567890abcdefghijklmn" # redefining `password` variable
  >>> if len(password) < 20: # Pythonic                                                                                                                                                                                            
  ...     print("Password is too short")
  ... else:
  ...     print("Password is long enough")
  ... 
  Password is long enough
  ```

### `elif` - "else if"

- Control-flow with `elif`

  ``` Python
  >>> password = "1234567890"
  >>> if len(password) < 5: # Pythonic
  ...     print("Password is too short")
  ... elif len(password) < 20:
  ...     print("Password is just right");
  ... else:
  ...     print("Password is too long")
  ...     
  Password is just right
  ```

### Combining and inverting booleans - `and`, `or`, `not`

- continued see [hartl](../README.md#hartl) p.51

- Combining and inverting booleans

  ``` Python
  >>> x = ''
  >>> y = 'y'
  >>> if len(x) == 0 and len(y) == 0:
  ...     print("x and y are empty")
  ... if len(x) == 0 or len(y) == 0:
  ...     print("x or y are empty")
  ... if not len(x) == 0:
  ...     print("x is not empty")
  ... if not len(y) == 0:
  ...     print("y is not empty")
  ... if not (len(x) == 0):
  ...     print("x is not empty")
  ... if (not len(y) == 0):
  ...     print("y is not empty")
  ... 
  x or y are empty
  y is not empty
  y is not empty
  ```

  ``` Python
  >>> x = 'x'
  >>> y = 'y'
  >>> if len(x) == 0 and len(y) == 0:
  ...     print("x and y are empty")
  ... if len(x) == 0 or len(y) == 0:
  ...     print("x or y are empty")
  ... if not len(x) == 0:
  ...     print("x is not empty")
  ... if not len(y) == 0:
  ...     print("y is not empty")
  ... if not (len(x) == 0):
  ...     print("x is not empty")
  ... if (not len(y) == 0):
  ...     print("y is not empty")
  ... 
  x is not empty
  y is not empty
  x is not empty
  y is not empty
  ```

  ``` Python
  >>> x = ''
  >>> y = ''
  >>> if len(x) == 0 and len(y) == 0:
  ...     print("x and y are empty")
  ... if len(x) == 0 or len(y) == 0:
  ...     print("x or y are empty")
  ... if not len(x) == 0:
  ...     print("x is not empty")
  ... if not len(y) == 0:
  ...     print("y is not empty")
  ... if not (len(x) == 0):
  ...     print("x is not empty")
  ... if (not len(y) == 0):
  ...     print("y is not empty")
  ... 
  x and y are empty
  x or y are empty
  ```

### Bang equals `!=`

- continued see [hartl](../README.md#hartl) p.54

- The same as above, using *bang equals*

  ``` Python
  >>> x = 'x'
  >>> if not len(x) == 0: # Not Pythonic!
  ...     print('x is not empty')
  ... if len(x) != 0: # Not quite Pythonic
  ...     print('x is not empty again')
  ... 
  x is not empty
  x is not empty again  
  ```

- In this case, it's more common to use `!=`  
  … This code is still not be considered fully *Pythonic*,  
  … because the empty string '' has a special value in **boolean context**.
