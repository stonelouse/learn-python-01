# 6. Functional Programming

- [6. Functional Programming](#6-functional-programming)
  - [6.1 List Comprehensions](#61-list-comprehensions)
    - [Concrete example and an *imperative* approach](#concrete-example-and-an-imperative-approach)
    - [Functional approach by applying *list comprehension*](#functional-approach-by-applying-list-comprehension)

## 6.1 List Comprehensions

- continued see [hartl](../README.md#hartl) p.150

- **List comprehensions** let us use functions to **build up lists** using a **single command**.

### Concrete example and an *imperative* approach

- Suppose we had a list of mixed-case strings, and we wanted to create a corresponding list of lowercase strings joined on a hyphen (making the result appropriate for use in URLs).

- The basic logic:

  ``` Python
  >>> state = "North Dakota"
  >>> state.lower()
  'north dakota'
  >>> state.lower().split()
  ['north', 'dakota']
  >>> "-".join(state.lower().split())
  'north-dakota'
  ```

  The use of the *combination* `.lower().split()`,  
  … which applies two methods in succession in a process
  … is known as **method chaining**.

- An *imperative* approach could look like this:

  - see `chp006_funcprog/package/p006_imperative_urls.py`  
    … and `chp006_funcprog/006.01.create_urls.py`

  ``` bash
  user@localhost:/mnt/ntfs1/home.UserRus/Documents.Notes/__learn-python-01/chp006_funcprog> python3 ./006.01.create_urls.py
  ['kansas', 'north-dakota', 'south-dakota', 'nebraska']
  ```

### Functional approach by applying *list comprehension*

- The second command is an example for *list comprehension*. We can think of an *transformation* as a **single operation**, and use a *list comprehension* to **apply the operation** in *sequence to each element* in the list, which is very flebile.

  ``` Python
  >>> list(range(10)) # applying the list() function
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  >>> [n for n in range(10)] # list comprehension
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  >>> [n*n for n in range(10)] # list comprehension is more flexible
  [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
  >>> states = ["Kansas", "North Dakota", "South Dakota", "Nebraska"]
  >>> [state.lower() for state in states]
  ['kansas', 'north dakota', 'south dakota', 'nebraska']
  >>> ["-".join(state.lower().split()) for state in states]
  ['kansas', 'north-dakota', 'south-dakota', 'nebraska']
  ```
  
  The 3rd command demonstrates that the *list comprehension* is more flexible than the `list()` function because **we can use it with other operations as well**, such as *squaring*.

- An *functional* approach could look like this:

  - see `chp006_funcprog/package/p006_02_functional_urls.py`  
    … and `chp006_funcprog/006.01.create_urls.py`

  ``` bash
  user@localhost:/mnt/ntfs1/home.UserRus/Documents.Notes/__learn-python-01/chp006_funcprog> python3 ./006.01.create_urls.py 
  Imperative: '['kansas', 'north-dakota', 'south-dakota', 'nebraska']'
  Functional: '['kansas', 'north-dakota', 'south-dakota', 'nebraska']'
  ```
