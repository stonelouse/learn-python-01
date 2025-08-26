# 2. String basics

- [2. String basics](#2-string-basics)
  - [2.4 Length, Boolean, and Control Flow](#24-length-boolean-and-control-flow)
    - [Boolean Context - `bool()`](#boolean-context---bool)
  - [2.5 Methods](#25-methods)
    - [`.find()` method and `in` operator](#find-method-and-in-operator)
  - [2.6 String Iteration](#26-string-iteration)
    - [Accessing a particular character – square brackets](#accessing-a-particular-character--square-brackets)
    - [`for` loop and `range()` function](#for-loop-and-range-function)
    - [`enumerate()` function](#enumerate-function)

## 2.4 Length, Boolean, and Control Flow

- continued see [hartl](../README.md#hartl) p.54

### Boolean Context - `bool()`

- Every Python object has a value of either `True` or `False` in a **boolean context**.
  … We can force Python **to use** such a *boolean context* with the **`bool()**` function.

- Most *things* that are in any sense *empty* are `False` in Python.  
  … **empty lists**, **empty tuples**, and **empty dictionaries** represents also `False`.

  ``` Python
  >>> bool('John Doe')
  True
  >>> bool(' ')
  True
  >>> bool('')
  False
  >>> bool(42)
  True
  >>> bool(0)
  False
  >>> 
  ```

- `if` or `elif` converts **all objects** to their *boolean equivalent* automatically.
  
  ``` Python
  >>> nobody = ''
  >>> if not nobody:
  ...     print ('nobody is empty and therefore `false` in a boolean context')
  ...     
  nobody is empty and therefore `false` in a boolean context
  ```

- Exercise 2.4.3
  
  ``` Python
  >>> x = 'foo'
  >>> y = ''
  >>> bool(x and y)
  False
  >>> if x and y:
  ...     print('`x` and `y` are both not empty')
  ... else:
  ...     print('Either `x` or `y` or both are empty')
  ...     
  Either `x` or `y` or both are empty
  
  >>> password = 'a' * 11
  >>> if len(password) > 10:
  ...     print(f'"{password}" has {len(password)} characters and is to long')
  ... else:
  ...     print(f'"{password}" is okay')
  ... 
  "aaaaaaaaaaa" has 11 characters and is to long
  >>> password = 'b' * 10
  >>> if len(password) > 10:
  ...     print(f'"{password}" has {len(password)} characters and is to long')
  ... else:
  ...     print(f'"{password}" is okay')
  ... 
  "bbbbbbbbbb" is okay
  ```

## 2.5 Methods

- continued see [hartl](../README.md#hartl) p.56

- In Python, *strings* are *objects* and provide **methods**.

  ``` Python
  >>> 'minion'.capitalize()
  'Minion'
  >>> 'minion'.capitalize # returns the raw method
  <built-in method capitalize of str object at 0x000002916FC61B30>
  >>> 'minion'.islower()
  True
  >>> 'minion'.isupper()
  False

  >>> m = 'minion'
  >>> m
  'minion'
  >>> m.uppercase()
  Traceback (most recent call last):
    File "<python-input-94>", line 1, in <module>
      m.uppercase()
      ^^^^^^^^^^^
  AttributeError: 'str' object has no attribute 'uppercase'
  >>> m.capitalize() # ☝returns a new string object without mutation the original string!
  'Minion'
  >>> m
  'minion'
  >>> m_upper = m.upper()
  >>> m_upper
  'MINION'
  >>> m_lower = m_upper.lower()
  >>> m_lower
  'minion'
  ```

- see <https://docs.python.org/3/library/stdtypes.html#string-methods>

### `.find()` method and `in` operator

- see <https://docs.python.org/3/library/stdtypes.html#str.find>
- see <https://python-reference.readthedocs.io/en/latest/docs/operators/in.html>

- To check if *sub* is a substring or not, use the [`in`](https://docs.python.org/3/reference/expressions.html#in) operator.

  ``` Python
  >>> m.find('ini') # `zero offset` or `zero-based indexing`
  1
  >>> m.find('uno') # not found
  -1
  >>> 'ini' in m # the `in` operator
  True
  >>> 'uno' in m
  False
  ```

- Exercise 2.5.1

  - [`.casefold()`](https://docs.python.org/3/library/stdtypes.html#str.casefold)
  - [`.strip()`](https://docs.python.org/3/library/stdtypes.html#str.split)
  
  ``` Python
  >>> "badger" in "hoNeY BaDGer".casefold()
  True
  >>> "  spacious  "
  '  spacious  '
  >>> "  spacious  ".strip()
  'spacious'
  ```

## 2.6 String Iteration

- see [hartl](../README.md#hartl) p.62

- In the case of string, we want to *iterate* one *character* at a time.  
  … First, we need to learn how to *access a particular character* in a string,  
  … and second, we need a *loop*.

  see [Common sequence operations | docs](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)

### Accessing a particular character – square brackets

- Using **square brackets** to access a particular character of a string
  
  ``` Python
  >>> soliloquy = 'To be or not to be, that is the question'
  >>> soliloquy[0] # `zero-offset` or `zero-based indexing`
  'T' 
  >>> soliloquy[3]
  'b' 
  >>> soliloquy[-1]
  'n' 
  ```

### `for` loop and `range()` function

- Using the [range()](https://docs.python.org/3/tutorial/controlflow.html#the-range-function) function to create a *sequence of numbers*

  ``` Python
  >>> for i in range(5):
  ...     print(i)
  ...     
  0
  1
  2
  3
  4
  ```

- Using a [**`for`**](https://wiki.python.org/moin/ForLoop) loop to iterate over a string in a **not Pythonic manner**
  
  ``` Python
  >>> for i in range(len(soliloquy)): # NOT Pythonic
  ...     print(soliloquy[i])
  ... 
  T
  o

  b
  e

  # …

  q
  u
  e
  s
  t
  i
  o
  n
  >>> 
  ```

- Using a **`for`** loop to iterate over a string in a **Pythonic manner**

  [String objects](https://docs.python.org/3/library/stdtypes.html#textseq) are [**iterable**](https://wiki.python.org/moin/Iterator) by itself
  
  ``` Python
  >>> for c in soliloquy: # Pythonic
  ...     print(c)
  ... 
  T
  o

  b
  e

  # …

  q
  u
  e
  s
  t
  i
  o
  n
  >>> 
  ```

- There are often **alternatives to looping**.

### `enumerate()` function

- Exercise 2.6.1

  ``` Python
  >>> print(soliloquy[::-1]) # slicing operation
  ... 
  noitseuq eht si taht ,eb ot ton ro eb oT
  >>> for c in soliloquy[::-1]:
  ...     print(c)
  ```

- GitHub Copilot: slicing operation
  
  >
  > - The code snippet:
  >
  >   ```python
  >   soliloquy[::-1]
  >   ```
  >
  >   is a Python **slicing operation** on a string (or any sequence).  
  >
  > - Here’s what it > does:
  >
  > - `soliloquy` is a variable, likely containing a string.
  > - `[::-1]` is **slice notation**:
  >   - The first two colons mean "take the whole string".
  >   - The `-1` means "step backwards", so it reverses the string.
  >
  > - So, `soliloquy[::-1]` returns the reversed version of the string stored in > `soliloquy`.
  >
  >   Example:
  >
  >   ```python
  >   soliloquy = "hello"
  >   print(soliloquy[::-1])  # Output: "olleh"
  >   ```
  >
  >   Note: The code as written is an expression, not a complete statement. To see > the result, you would need to print it or assign it to another variable.

- Alternatively, we can use the [`reversed()`](https://docs.python.org/3/library/functions.html#reversed) *fn*, which returns an **iterator** which we can use to create a *string*

  ``` Python
  >>> soliloquy = "hello"
  >>> ''.join(reversed(soliloquy))
  'olleh'
  ```

- The *Pythonic* way to iterate over the characters of a string and having access to the character's index – [**`enumerate()`**](https://docs.python.org/3/library/functions.html#enumerate) function:

  ``` Python
  >>> for i, c in enumerate(soliloquy):
  ...  print(f"Char '{i + 1}' is '{c}'")
  ... 
  Char '1' is 'T'
  Char '2' is 'o'
  Char '3' is ' '
  Char '4' is 'b'
  Char '5' is 'e'
  Char '6' is ' '
  Char '7' is 'o'
  Char '8' is 'r'
  Char '9' is ' '
  # …  
  ```
