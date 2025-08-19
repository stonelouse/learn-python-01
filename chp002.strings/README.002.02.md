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

- xxx

  ``` Python
  >>> password = "1234567890"
  >>> if len(password) < 5: # Pythonic
  ...     print("Password is too short")
  ... elif len(password) < 20:
  ...     print("Password is just right");
  ... else:
  ...     print("Passowrd is too long")
  ...     
  Password is just right
  ```
