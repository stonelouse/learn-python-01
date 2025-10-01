# 6. Functional Programming

- Todo

## 6.3 Dictionary Comprehensions

- continued see [hartl](../README.md#hartl) p.159

- Now, we want to create a *dictionary* that associates the state names to the length of each name.

### Concrete example and an *imperative* approach

- First the *imperative* approach

  ``` Python
  >>> def imperative_length(states):
  ...   lengths = {}
  ...   for state in states:
  ...     lengths[state] = len(state)
  ...   return lengths
  ...
  >>> states = ["Kansas", "Nebraska", "North Dakota", "South Dakota"]
  >>> print(imperative_length(states))
  {'Kansas': 6, 'Nebraska': 8, 'North Dakota': 12, 'South Dakota': 12}
  ```

### *Functional approach* by applying *dictionary comprehension*

- The *functional* approach

  ``` Python
  >>> def functional_length(states):
  ...   return {state: len(state) for state in states}
  ... 
  >>> print(functional_length(states))
  {'Kansas': 6, 'Nebraska': 8, 'North Dakota': 12, 'South Dakota': 12}
  ```

- For *dictionary comprehensions*, we just use  
  … **curly braces** instead of *square brackets* and  
  … a **key–value** pair instead of a *single element*.

- Exercise 6.3.1
  
  - see `chp006_funcprog/package/p006_03_exercise_6_3_1.py`

  - `user@linux:/mnt/ntfs1/home.UserRus/Documents.Notes/__learn-python-01> python3`

    ``` Python
    >>> import importlib
    >>> import chp006_funcprog.package.p006_03_exercise_6_3_1 as states_module
    >>> states = ["Kansas", "North Dakota", "South Dakota", "Nebraska"]
    >>> states_module.states_to_url(states)
    {'Kansas': 'kansas', 'North Dakota': 'north-dakota', 'South Dakota': 'south-dakota', 'Nebraska': 'nebraska'}
    ```
