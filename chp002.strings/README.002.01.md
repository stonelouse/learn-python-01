# 2. String basics

- [2. String basics](#2-string-basics)
  - [2.1 String Basics](#21-string-basics)
    - [Characters](#characters)
    - [String Literals](#string-literals)
    - [Quotes](#quotes)
    - [Triple-Quoted strings](#triple-quoted-strings)
  - [2.2 Concatenation and Interpolation](#22-concatenation-and-interpolation)
    - [Variables](#variables)
    - [Formatted Strings – `str.format()` –  `%`](#formatted-strings--strformat---)
    - [Raw Strings](#raw-strings)
    - [Formatted Triple-quoted Strings](#formatted-triple-quoted-strings)

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
  
  # Exercise 2.1.1
  >>> 'It\'s not "easy" being green'
  'It\'s not "easy" being green'
  >>> print('It\'s not "easy" being green')
  It's not "easy" being green
  >>> 'hello\tgoodbye'
  'hello\tgoodbye'
  >>> print('hello\tgoodbye')
  hello   goodbye
  >>> 'hello\ngoodbye'
  'hello\ngoodbye'
  >>> print('hello\ngoodbye')
  hello  
  goodbye
  # ☝ Notice the special 'r' behavior!
  >>> r'hello\ngoodbye'
  'hello\\ngoodbye'
  >>> print(r'hello\ngoodbye')
  hello\ngoodbye
  >>> print("hello\ngoodbye")
  hello
  goodbye
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

## 2.2 Concatenation and Interpolation

- see [hartl](../README.md#hartl) p.38

- can be accomplished using the `+`-operator.
  
  ``` Python
  # see https://www.learnenough.com/command-line-tutorial/manipulating_files#aside-foo-bar
  >>> "foo" + "bar"
  'foobar'
  >>> first_name = "John"
  >>> last_name = "Doe"
  >>> first_name + ", " + last_name
  'John, Doe'  
  ```

### Variables

- are written in **snake case**

### Formatted Strings – `str.format()` –  `%`

- see [hartl](../README.md#hartl) p.41

- Most *pythonic* way to build up strings is
  … via *interpolation* using **formatted strings**, or **f-strings**

  ``` Python
  >>> first_name = "John"
  >>> last_name = "Doe"
  # … using formatted strings; since Python 3.6
  >>> f"{first_name}, {last_name}" 
  'John, Doe'
  # … using str.format(); see https://realpython.com/python-f-strings/
  >>> "{}, {}".format(first_name, last_name) 
  'John, Doe'
  # … using '%' formatting
  >>> "%s, %s" % (first_name, last_name)
  'John, Doe'
  ```

### Raw Strings

- Raw strings are **truly literal**  
  … containing exactly the characters you type.  
  … For example, Python **won't interpolate** into *raw strings* () or in *regular strings*.

  ``` Python
  >>> first_name = "John"
  >>> last_name = "Doe"
  # Formatted string
  >>> f"{first_name}, {last_name}"
  'John, Doe'
  # Regular string
  >>> "{first_name}, {last_name}"
  '{first_name}, {last_name}'
  # Raw string
  >>> r"{first_name}, {last_name}"
  '{first_name}, {last_name}'  
  ```

  ``` Python
  >>> "{first_name}\n{last_name}"
  '{first_name}\n{last_name}'
  >>> print("{first_name}\n{last_name}")
  {first_name}
  {last_name} 
  >>> "{first_name}\\n{last_name}"
  '{first_name}\\n{last_name}'
  >>> print("{first_name}\\n{last_name}")
  {first_name}\n{last_name}
  >>> r"{first_name}\n{last_name}"
  # REPL escapes 'backslash n' combination
  '{first_name}\\n{last_name}'
  # literal 'backslash n' combination with raw string
  >>> print(r"{first_name}\n{last_name}")
  {first_name}\n{last_name}
  ```

### Formatted Triple-quoted Strings

- … also support interpolation

  ``` Python
  '''{first_name},
  ... {last_name}'''
  '{first_name},\n{last_name}'
  >>> print('''{first_name},
  ... {last_name}''')
  {first_name},
  {last_name}
  >>> f'''{first_name},
  ... {last_name}'''
  'John,\nDoe'
  >>> print(f'''{first_name},
  ... {last_name}''')
  John,
  Doe
  ```
