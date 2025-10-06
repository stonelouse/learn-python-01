# 6. Functional Programming

- [6. Functional Programming](#6-functional-programming)
  - [6.5 Other Functional Techniques](#65-other-functional-techniques)
    - [Built-in Functions - Summing elements i a *list* or *range*](#built-in-functions---summing-elements-i-a-list-or-range)
      - [Imperative approach](#imperative-approach)
      - [Functional approach](#functional-approach)
    - [Built-in Functions - Multiplying elements i a *list* or *range*](#built-in-functions---multiplying-elements-i-a-list-or-range)
    - [`itertools` Module](#itertools-module)
    - [Functional Programming and TDD](#functional-programming-and-tdd)

## 6.5 Other Functional Techniques

- continued see [hartl](../README.md#hartl) p.165

- Python includes many other functional techniques.

### Built-in Functions - Summing elements i a *list* or *range*

#### Imperative approach

- Imperative Approach for summing integers

  ``` Python
  >>> def imperative_sum(numbers):
  ...   total = 0
  ...   for number in numbers:
  ...     total += number
  ...   return total
  ...
  >>> print(imperative_sum(range(1,4)))
  6
  ```

#### Functional approach

- The functional (and very Pythonic) solution is to use the built-in [**`sum()`**](https://docs.python.org/3/library/functions.html#sum) *fn*.

  ``` Python
  >>> sum(range(1,4))
  6
  ```

### Built-in Functions - Multiplying elements i a *list* or *range*

- Applying [**`math.prod()`**](https://docs.python.org/3/library/math.html#math.prod) to a *iterable*

  ``` Python
  >>> from math import prod
  >>> prod(range(1,4))
  6
  ```

### `itertools` Module

- The [**`itertools`**](https://docs.python.org/3/library/itertools.html) module includes a large variety of similar tools.

  > This module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an “**iterator algebra**” making it possible to construct specialized tools succinctly and efficiently in pure Python.

### Functional Programming and TDD

- see [hartl](../README.md#hartl) p.166

- A common situation is to write an *imperative solution* for a particular task, only to discover later on that there’s a *functional way* to do it. But
making changes to working code can be risky, which might make us understandably
reluctant to change to the functional version.  
  
  My favorite *technique for managing this challenge* is **test-driven development (TDD)**, which involves writing an *automated test* that **captures the desired behavior** in code.

- Exercise 6.5.2

  ``` Python
  >>> import math
  >>> math.factorial(10)
  3628800
  >>> math.prod(range(1,11))
  3628800
  ```
