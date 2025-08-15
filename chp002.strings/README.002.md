# 2. String basics

- [2. String basics](#2-string-basics)
  - [2.1 String Basics](#21-string-basics)
    - [Characters](#characters)
    - [String Literals](#string-literals)
    - [Quotes](#quotes)
    - [Triple-Quoted strings](#triple-quoted-strings)

## 2.1 String Basics

- see [hartl](../README.md#hartl) p.35

### Characters

- Like many other high-level languages, Python "characters" are just *strings of length one*. This stands in contrast to lower-level languages like C and Java, which have a special type just for characters.

### String Literals

- A sequence of characters typed literally is called a **string literal**.

### Quotes

- *Single* quotes and *double* quotes are almost the same in Python.

  ``` Python
  >>> ""
  ''  # just a convention in REPL; double-quoted strings are converted in single-quoted strings
  >>> ''
  ''  
  >>> "It's not easy being green"
  "It's not easy being green"
  >>> 'It is written "Python"'
  'It is written "Python"'
  >>>
  ```

### Triple-Quoted strings

- see [hartl](../README.md#hartl) p.37

- can contain **newlines**

  ``` Python
  >>> """This is line 1
  ... This is line 2
  ... This is line 3"""
  'This is line 1\nThis is line 2\nThis is line 3'
  >>> print("""This is line 1
  ... This is line 2
  ... This is line 3""")
  This is line 1
  This is line 2
  This is line 3
  >>>
  ```

- Triple-quoted strings are notable for their use in *docstrings*,  
  … which are special documentation strings used in Python functions and classes.

- [PEP 8](../README.md#pep-8) indicates that  
  … *single-quoted* and *double-quoted* strings are both acceptable as long as you're consistent,  
  … BUT *triple-quoted* strings should always use the ***double-quoted*** variant.
