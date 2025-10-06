# Learning Python

- [Learning Python](#learning-python)
  - [References](#references)
    - [hartl](#hartl)
  - [Links](#links)
    - [PEP 8](#pep-8)
    - [Some Python Doc Sides](#some-python-doc-sides)
    - [Emojis](#emojis)
  - [Notes](#notes)
    - [Pythonic/ unPythonic programming](#pythonic-unpythonic-programming)
    - [Notable differences between Python and most other languages](#notable-differences-between-python-and-most-other-languages)
    - [*"Literals"* vs. *Comprehensions*](#literals-vs-comprehensions)
  - [Overview](#overview)
    - [Chapter 1](#chapter-1)
    - [Chapter 2 - String Basics](#chapter-2---string-basics)
    - [Chapter 3 - Lists](#chapter-3---lists)
    - [Chapter 4 - Other Native Objects](#chapter-4---other-native-objects)
    - [Chapter 5 - Functions and Iterators](#chapter-5---functions-and-iterators)
    - [Chapter 6 - Functional Programming](#chapter-6---functional-programming)

## References

### hartl

- Hartl, Michael: Learn enough Python to be dangerous, Humble Bundle Pearson, 2023  
  [Source Code | GitHub](https://github.com/learnenough/learn_enough_python_code_listings)

## Links

### PEP 8

- [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)

### Some Python Doc Sides

- [Index | docs](https://docs.python.org/3/genindex.html)
- [Built-in Functions | docs](https://docs.python.org/3/library/functions.html)
- [Built-in Types | docs](https://docs.python.org/3/library/stdtypes.html)
- [5. Data Structures | docs](https://docs.python.org/3/tutorial/datastructures.html)
- [8. Compound statements | docs](https://docs.python.org/3/reference/compound_stmts.html)

### Emojis

- [emojipedia](https://emojipedia.org/)

## Notes

### Pythonic/ unPythonic programming

- see [hartl](#hartl) p.2

### Notable differences between Python and most other languages

- see [hartl](#hartl) p.6

### *"Literals"* vs. *Comprehensions*

``` Python
["ant", "bear", "spider"]                        # Literal list
("ant", "bear", "spider")                        # Literal tuple
{1, 2, 3, 3, 4, 1}                               # Literal set
{"stop": "red", "wait": "yellow", "go": "green"} # Literal dictionary

[]                                               # empty list
()                                               # empty tuple
{}                                               # empty dictionary
set()                                            # empty set

states = ["Kansas", "North Dakota", "Nebraska", "South Dakota"]
# List comprehension ➡️ ['north-dakota', 'south-dakota']
["-".join(state.lower().split()) for state in states if len(state.split()) > 1]

# Dictionary comprehension ➡️ {6: 'Kansas', 8: 'Nebraska'}
{len(state): state for state in states if len(state.split()) == 1}

", ".join(
...   # Generator comprehension ➡️ 'kansas, nebraska'
...   state.lower() for state in states if len(state.split()) == 1
... )

>>> from itertools import chain
>>> list(chain.from_iterable([state.split() for state in states]))
['Kansas', 'North', 'Dakota', 'Nebraska', 'South', 'Dakota']
# Set comprehension
>>> {element for element in list(chain.from_iterable([state.split() for state in states]))}
{'Kansas', 'South', 'Dakota', 'Nebraska', 'North'}
```

## Overview

### Chapter 1

- [1.2 Python in a REPL](./chp001/README.001.md#12-python-in-a-repl)
- [1.2 Python in a File](./chp001/README.001.md#13-python-in-a-file)
- [1.2 Python in a Shell Script](./chp001/README.001.md#14-python-in-a-shell-script)
- [1.2 Python in a Web Server](./chp001/README.001.md#15-python-in-a-web-server)

### Chapter 2 - String Basics

- [2.1 String Basics](./chp002.strings/README.002.01.md#21-string-basics)
- [2.2 String Concatenation and Interpolation](./chp002.strings/README.002.01.md#22-concatenation-and-interpolation)
- [2.3 Printing](./chp002.strings/README.002.02.md#23-printing)
- [2.4 Length, Booleans, and Control Flow](./chp002.strings/README.002.02.md#24-length-boolean-and-control-flow)
- [2.4 Length, Booleans, and Control Flow | Boolean Context](./chp002.strings/README.002.03.md#24-length-boolean-and-control-flow)
- [2.5 Methods](./chp002.strings/README.002.03.md#25-methods)
- [2.6 String Iteration](./chp002.strings/README.002.03.md#26-string-iteration)

### Chapter 3 - Lists

- [3.1 Splitting](./chp003.lists/README.003.01.md#31-splitting)
- [3.2 List Access](./chp003.lists/README.003.01.md#32-list-access)
- [3.3 List Slicing](./chp003.lists/README.003.02.md#33-list-slicing)
- [3.4 More List Techniques](./chp003.lists/README.003.02.md#34-more-list-techniques)
  - [3.4.1 Element Inclusion](./chp003.lists/README.003.02.md#341-element-inclusion)
  - [3.4.2 Sorting, Reversing, and Comparison](./chp003.lists/README.003.02.md#342-sorting-reversing-and-comparison)
  - [3.4.3 Appending and Popping](./chp003.lists/README.003.02.md#343-appending-and-popping)
  - [3.4.4 Undoing a Split - Join](./chp003.lists/README.003.02.md#344-undoing-a-split---join)
- [3.5 List Iteration](./chp003.lists/README.003.03.md#35-list-iteration)
- [3.6 Tuples and Sets](./chp003.lists/README.003.04.tuples&set.md#36-tuples-and-sets)

### Chapter 4 - Other Native Objects

- [4.1 Math](./chp004.other-native-object/README.004.01.math.md#41-math)
- [4.2 Time and Datetime](./chp004.other-native-object/README.004.02.date-time.md#42-time-and-datetime)
- [4.3 Regular Expressions](./chp004.other-native-object/README.004.03.regex.md#43-regular-expressions---regex)
- [4.4 Dictionaries](./chp004.other-native-object/README.004.04.dictionaries.md#44-dictionaries)
- [4.5 Application - Unique Words](./chp004.other-native-object/README.004.05.exercise.unique-words.md)

### Chapter 5 - Functions and Iterators

- [5.1 Function Definitions](./chp005_functions_iterators/README.005.01.func.md#51-function-definitions)
- [5.1.1 First Class Functions](./chp005_functions_iterators/README.005.01.func.md#511-first-class-functions)
- [5.1.2 Variable and Keyword Arguments](./chp005_functions_iterators/README.005.01.func.md#512-variable-and-keyword-arguments)
- [5.2 Functions in a file](./chp005_functions_iterators/README.005.01.func.md#52-functions-in-a-file)
- [5.3 Iterators](./chp005_functions_iterators/README.005.02.iterators.md#53-iterators)
- [5.3.1 Generators](./chp005_functions_iterators/README.005.03.generators.md#531-generators)

### Chapter 6 - Functional Programming

- [6.1 List Comprehensions](./chp006_funcprog/README.006.01.funcprog.list-comprehensions.md#61-list-comprehensions)
- [6..2 List Comprehensions with Conditions](./chp006_funcprog/README.006.01.funcprog.list-comprehensions.md#62-list-comprehensions-with-conditions)
- [6.3 Dictionary Comprehensions](./chp006_funcprog/README.006.02.funcprog.dict-comprehensions.md#63-dictionary-comprehensions)
- [6.4 Generator and Set Comprehensions](./chp006_funcprog/README.006.03.funcprog.generator-set-comprehensions.md#64-generator-and-set-comprehensions)
- [6.4.1 Generator Comprehensions](./chp006_funcprog/README.006.03.funcprog.generator-set-comprehensions.md#641-generator-comprehensions)
- [6.4.2 Set Comprehensions](./chp006_funcprog/README.006.03.funcprog.generator-set-comprehensions.md#642-set-comprehensions)
- [6.5 Other Functional Techniques](./chp006_funcprog/README.006.04.funcprog.other-func-techniques.md)
