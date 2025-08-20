# 2. String basics

- [2. String basics](#2-string-basics)
  - [2.4 Length, Boolean, and Control Flow](#24-length-boolean-and-control-flow)
    - [Boolean Context - `bool()`](#boolean-context---bool)
  - [2.5 Methods](#25-methods)

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
  >>>
  ```
