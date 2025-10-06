# 6. Functional Programming

- [6. Functional Programming](#6-functional-programming)
  - [6.1 List Comprehensions](#61-list-comprehensions)
    - [Concrete example and an *imperative* approach (with conditions)](#concrete-example-and-an-imperative-approach-with-conditions)
    - [*Functional approach* by applying *list comprehension*](#functional-approach-by-applying-list-comprehension)
  - [6.2 List Comprehensions with Conditions](#62-list-comprehensions-with-conditions)
    - [Concrete example and an *imperative* approach](#concrete-example-and-an-imperative-approach)
    - [*Functional approach* by applying *list comprehension with condition*](#functional-approach-by-applying-list-comprehension-with-condition)

## 6.1 List Comprehensions

- continued see [hartl](../README.md#hartl) p.150

- **List comprehensions** let us use functions to **build up lists** using a **single command**.

### Concrete example and an *imperative* approach (with conditions)

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

### *Functional approach* by applying *list comprehension*

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

## 6.2 List Comprehensions with Conditions

- continued see [hartl](../README.md#hartl) p.156

- In addition to supporting the creation of *lists* using `for`,  
  … Python *list comprehensions* also support the use of **conditions** using **`if`**  
  … to *select* only elements satisfying particular criteria.

### Concrete example and an *imperative* approach

- Now, we wanted to select the strings in our `states` list that consist of only one word:

  ``` Python
  >>> def imperative_singles(states):
  ...   singles = []
  ...   for state in states:
  ...     if len(state.split()) == 1:
  ...       singles.append(state)
  ...   return singles
  ... 
  >>> states = ["Kansas", "North Dakota", "South Dakota", "Nebraska"]
  >>> print(imperative_singles(states))
  ['Kansas', 'Nebraska']
  ```

### *Functional approach* by applying *list comprehension with condition*

- List comprehension with condition

  ``` Python
  >>> def functional_singles(states):
  ...   return [state for state in states if len(state.split()) == 1]
  ... 
  >>> print(functional_singles(states))
  ['Kansas', 'Nebraska']
  ```

- As compact as *list comprehensions* can be, it’s worth noting that there are limitations to their use.
  
  In particular, as the *logic* inside *list comprehensions* gets **more complicated**, they can quickly become unwieldy. It is therefore considered *unPythonic* to build up *complicated list comprehensions*; if you find yourself trying to squeeze too much content into a single comprehension, consider using a good old-fashioned `for` loop instead.

- Exercise 6.2.1

  ``` Python
  >>> def dakotas_with_in(states):
  ...   return [state for state in states if "Dakota" in state]
  ...
  >>> print (dakotas_with_in(states))
  ['North Dakota', 'South Dakota']

  >>> def dakotas_with_split(states):
  ...   return [state for state in states if len(state.split()) > 1]
  ... 
  >>> print(dakotas_with_split(states))
  ['North Dakota', 'South Dakota']
  ```  
