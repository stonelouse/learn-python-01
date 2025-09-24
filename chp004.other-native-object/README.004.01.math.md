# 4. Other Native Objects

- [4. Other Native Objects](#4-other-native-objects)
  - [4.1 Math](#41-math)
    - [4.1.1 More Advanced Operations](#411-more-advanced-operations)
    - [4.1.2 Math to String – `str()`, `int()`, `float()`, (and `map()`)](#412-math-to-string--str-int-float-and-map)
  - [Retrieving the result of the previously executed command in REPL - "**`_`**"](#retrieving-the-result-of-the-previously-executed-command-in-repl---_)
  - [Importing specific items from a module](#importing-specific-items-from-a-module)

## 4.1 Math

- see [hartl](../README.md#hartl) p.91

- Python supports a large number of *mathematical operations*

  ``` Python
  >>> 41 + 1
  42  
  >>> 43 - 1
  42  
  >>> 84 / 2
  42.0
  >>> 84 // 2 # ☝ Integer division
  42  
  >>> 42 / 84
  0.5 
  >>> 42 // 84 # ☝ Integer division
  0   
  >>> 21 * 2
  42
  ```

  Because of its great numerical capabilities, many programmers, find it convenient to fire up a Python interpreter and use it as a simple calculator when the need arises.

### 4.1.1 More Advanced Operations

- see [hartl](../README.md#hartl) p.92

- Python provides a [**`math`**](https://docs.python.org/3/library/math.html) module, which provides *more advanced mathematical operations*.

- To use the functionality of a module, we have to **load the module** using the [**`import`**](https://docs.python.org/3/reference/simple_stmts.html#import) statement  
  … and then access the module contents using its ***prefix*** `<module-name>.`.  
  … The *prefix* represents the modules' **namespace**.

  ``` Python
  >>> import math
  >>> math.cos(1)
  0.5403023058681397
  >>> math.cos(math.pi)
  -1.0
  
  >>> math.cos(math.pi/4)
  0.7071067811865476
  >>> math.cos(math.pi/2)
  6.123233995736766e-17
   
  >>> math.cos(0)
  1.0 
  
  >>> math.cos(math.pi)
  -1.0
  
  >>> math.cos(0.5*math.pi)
  6.123233995736766e-17
  
  # Like most other programming languages, Python use `log(x)` for 'ln x'
  >>> math.log(math.e)
  1.0 
  
  # represents log₁₀
  >>> math.log10(10) 
  1.0 
  
  # Using underscores in big numbers
  >>> math.log10(1_000_000)
  6.0 
  ```

### 4.1.2 Math to String – `str()`, `int()`, `float()`, (and `map()`)

- [`str()`](https://docs.python.org/3/library/functions.html#func-str), [`int()`](https://docs.python.org/3/library/functions.html#int), [`float()`](https://docs.python.org/3/library/functions.html#float) and [`map()`](https://docs.python.org/3/library/functions.html#map) in action

  ``` Python
  >>> ls = ["2", "4", "6"]
  >>> li = []
  # `int()`: Converting string to int
  >>> for s in ls:
  ...     li.append(int(s))
  ...     
  >>> li
  [2, 4, 6]
  >>> import math
  # Creating a list of floats
  >>> lf = []
  >>> for i in li:
  ...     lf.append(i * math.pi)
  ...     
  >>> lf
  [6.283185307179586, 12.566370614359172, 18.84955592153876]
  # `str()`: Converting float to string
  >>> for i, f in enumerate(lf):
  ...     ls[i] = str(f)
  ... 
  >>> ls
  ['6.283185307179586', '12.566370614359172', '18.84955592153876']
  # `float()`: Converting string to float (with `map()` and the help of Copilot)
  >>> lf2 = list(map(float, ls))
  >>> lf2
  [6.283185307179586, 12.566370614359172, 18.84955592153876]
  # `int()`: Transform float to int
  >>> int(lf2[0])
  6  
  >>> li2 = list(map(int, lf2))
  >>> li2
  [6, 12, 18]
  ```

## Retrieving the result of the previously executed command in REPL - "**`_`**"

- Retrieving the result of the previously executed command in the REPL using the ***underscore***:

  ``` Python
  # …
  >>> li2 = list(map(int, lf2))
  >>> li2
  [6, 12, 18]
  >>> # Retrieving the result of the previously executed command in the REPL
  >>> _[1]
  12  
  ```

## Importing specific items from a module

- Importing specific items from a module

  ``` Python
  >>> from math import cos, sin # ☝ Pythonic
  >>> sin(math.pi/2)
  1.0
  >>> cos(math.pi)
  -1.0
  ```

- Importing all items from a module ☝ **DISCOURAGED**

  ``` Python
  >>> from math import * # ☝ Not Pythonic and DANGEROUS
  >>> cos(pi)
  -1.0  
  ```

  This carries a **high risk of (*name*) collisions**!

- Exercise 4.1.3

  ``` Python
  >>> float("1.24e6")
  1240000.0
  >>> str(_)
  '1240000.0'
  >>> int(6.28) == int(6.98)
  True
  >>>
  >>> from math import floor
  >>> x = floor(6.28)
  >>> x
  6   
  >>> y = floor(6.98)
  >>> y
  6
  ```
