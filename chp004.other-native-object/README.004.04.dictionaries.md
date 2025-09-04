# 4. Other Native Objects

- [4. Other Native Objects](#4-other-native-objects)
  - [4.4 Dictionaries](#44-dictionaries)
    - [Creating a dictionary](#creating-a-dictionary)
    - [`.get()` method](#get-method)
    - [Literal curly braces syntax](#literal-curly-braces-syntax)
    - [Using `dict()` *fn* to create dictionaries](#using-dict-fn-to-create-dictionaries)
    - [`.keys()` and `.values()`](#keys-and-values)

## 4.4 Dictionaries

- continued see [hartl](../README.md#hartl) p.109

- You can think of *dictionaries* as being like *lists*  
  … but with **generic labels** rather then *integers as indices*.

  Each element is thus a pair of values (*key-value pairs*):  
  … a label (the *key*)  
  … an element of any type (the *value*)

- Like a *list index*, a *dictionary key* **maps to only one value at a time**.  
  … This means that we can replace the value corresponding to a *key*  
  … but we **can’t have two identical keys**.

### Creating a dictionary

- An empty dictionary is represented by *empty* **curly braces**

  ``` Python
  >>> user = {}
  # Element access is like lists
  >>> user["first_name"] = "John"
  >>> user["last_name"] = "Doe"
  >>> user["first_name"]
  'John'
  >>> user["last_name"]
  'Doe'
  >>> user["unknown_name"]
  Traceback (most recent call last):
    File "<python-input-6>", line 1, in <module>
      user["unknown_name"]
      ~~~~^^^^^^^^^^^^^^^
  KeyError: 'unknown_name'
  >>> 
  ```

  Since an empty dictionary is represented by curly braces, we have to use the [`set()`](../chp003.lists/README.003.04.tuples&set.md#empty-lists-tuples-or-sets-are-false-in-a-boolean-context) *fn* to create an *empty set*.

### `.get()` method

- Since a error is raised if the key does not exist, the [`dict.get()`](https://docs.python.org/3/library/stdtypes.html#dict.get) method may be more convenient:

  ``` Python
  >>> # …
  >>> user.get("unknown_name")
  >>> user.get("unknown_name") == None
  True
  >>> repr(user.get("unknown_name"))
  'None'
  >>> user.get("first_name")
  'John'
  >>>
  ```

### Literal curly braces syntax

- Literal curly braces syntax can be used to define *dictionaries* literally

  ``` Python
  >>> repr(user)
  "{'first_name': 'John', 'last_name': 'Doe'}"
  >>> state = {"stop": "red", "wait": "yellow", "go": "green"}
  >>> state["stop"] 
  'red'
  >>> state.get("go")
  'green'
  >>> repr(state)
  "{'stop': 'red', 'wait': 'yellow', 'go': 'green'}"
  >>>
  ```

  If we take a look at how *dictionaries* are represented, we see that they consist of
*keys* and *values* separated by **colons**

### Using `dict()` *fn* to create dictionaries

- Using [`dict()`](https://docs.python.org/3/library/stdtypes.html#dict) *fn* to create dictionaries:

  ``` Python
  >>> state_alt = dict(stop=1, wait=2, go=3)
  >>> repr(state_alt)
  "{'stop': 1, 'wait': 2, 'go': 3}"
  >>> state_alt["stop"]
  1
  >>> state_alt["go"]
  3
  >>>
  ```

### `.keys()` and `.values()`

- We can look at the keys and values separately, which (as of Python 3.6 and later) are
**stored in order** in *special-purpose* Python objects:

  ``` Python
  >>> moonwalks = {
  ... "Neil Armstrong": 1969,
  ... "Buzz Aldrin": 1969,
  ... "Alan Shepard": 1971,
  ... "Eugene Cernan": 1972,
  ... "Michael Jackson": 1983
  ... }
  >>> moonwalks.keys()
  dict_keys(['Neil Armstrong', 'Buzz Aldrin', 'Alan Shepard', 'Eugene Cernan', 'Michael Jackson'])
  >>> moonwalks.values()
  dict_values([1969, 1969, 1971, 1972, 1983])
  ```

- see [`.values()`](https://docs.python.org/3/library/stdtypes.html#dict.values)
  … technically, returns a new *view* of the dictionaries values

- see [`.keys()](https://docs.python.org/3/library/stdtypes.html#dict.keys)
  … technically, returns a new *view* of the dictionaries keys

  The *special-purpose* objects returned by the `.keys()` method can be treated like a [`set`](../chp003.lists/README.003.04.tuples&set.md#sets) **in some contexts**:

  ``` Python
  # …
  >>> apollo_11 = {"Neil Armstrong", "Buzz Aldrin", "John Doe"} # A set
  >>> moonwalks.keys() & apollo_11 # Intersection
  {'Neil Armstrong', 'Buzz Aldrin'}
  ```

- Test for inclusion:
  
  ``` Python
  # …
  >>> "Buzz Aldrin" in moonwalks
  True
  >>> "John Doe" in moonwalks
  False
  ```
