# 4. Other Native Objects

- [4. Other Native Objects](#4-other-native-objects)
  - [4.4 Dictionaries](#44-dictionaries)
    - [Creating a dictionary](#creating-a-dictionary)
    - [`.get()` method](#get-method)
    - [Literal curly braces syntax](#literal-curly-braces-syntax)
    - [Using `dict()` *fn* to create dictionaries](#using-dict-fn-to-create-dictionaries)
    - [`.keys()` and `.values()`](#keys-and-values)
    - [4.4.1 Dictionary Iteration](#441-dictionary-iteration)
      - [`dict.items()`](#dictitems)
    - [4.4.2 Merging dictionaries](#442-merging-dictionaries)
      - [Strange-looking `**` syntax and *pipe* operator](#strange-looking--syntax-and-pipe-operator)
    - [Applying `enumerate()` to `dict.items()`](#applying-enumerate-to-dictitems)

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

### 4.4.1 Dictionary Iteration

- continued see [hartl](../README.md#hartl) p.112

- As with lists, tuples, and sets, one of the most common dictionary tasks is iterating over elements.

  ``` Python
  >>> moonwalks = {
  ... "Neil Armstrong": 1969,
  ... "Buzz Aldrin": 1969,
  ... "Alan Shepard": 1971,
  ... "Eugene Cernan": 1972,
  ... "Michael Jackson": 1983
  ... }
  >>> for key in moonwalks.keys():    # NOT Pythonic
  ...     print(f"{key} first performed a moonwalk in {moonwalks[key]}.")
  ...     
  Neil Armstrong first performed a moonwalk in 1969. 
  Buzz Aldrin first performed a moonwalk in 1969.    
  Alan Shepard first performed a moonwalk in 1971.   
  Eugene Cernan first performed a moonwalk in 1972.  
  Michael Jackson first performed a moonwalk in 1983.
  ```

- Iterating over keys is the default

  ``` Python
  >>> for key in moonwalks: # Somewhat Pythonic; iterating over keys is the default
  ...     print(f"{key} first performed a moonwalk in {moonwalks[key]}.")
  ... 
  Neil Armstrong first performed a moonwalk in 1969.
  Buzz Aldrin first performed a moonwalk in 1969.
  Alan Shepard first performed a moonwalk in 1971.
  Eugene Cernan first performed a moonwalk in 1972.
  Michael Jackson first performed a moonwalk in 1983.
  ```

#### `dict.items()`

- [**`dict.items()`**](https://docs.python.org/3/library/stdtypes.html#dict.items) returns a new [view](https://docs.python.org/3/library/stdtypes.html#dict-views) of dictionary items.

  ``` Python
  >>> moonwalks.items()
  dict_items([('Neil Armstrong', 1969), ('Buzz Aldrin', 1969), ('Alan Shepard', 1971), ('Eugene Cernan', 1972), ('Michael Jackson', 1983)])
  >>> type(moonwalks.items())
  <class 'dict_items'>
  >>> for name, year in moonwalks.items(): # Very Pythonic
  ...     print(f"{name} first performed a moonwalk in {year}.")
  ... 
  Neil Armstrong first performed a moonwalk in 1969.
  Buzz Aldrin first performed a moonwalk in 1969.
  Alan Shepard first performed a moonwalk in 1971.
  Eugene Cernan first performed a moonwalk in 1972.
  Michael Jackson first performed a moonwalk in 1983.
  ```

### 4.4.2 Merging dictionaries

- continued see [hartl](../README.md#hartl) p.113

- One common operation is merging dictionaries, where the elements of two dictionaries
are combined into one.

#### Strange-looking `**` syntax and *pipe* operator

- Two ways to merge dictionaries

  ``` Python
  >>> dict1 = {
  ...   "one": 1, "two": 2, "three": 3
  ... }
  >>> dict2 = {
  ...   "four": "FOUR", "two": "TWO", "five": "FIVE"
  ... }
  >>> merge1 = {**dict1, **dict2} # Kind of Pythonic; pretty strange-looking syntax
  >>> merge1
  {'one': 1, 'two': 'TWO', 'three': 3, 'four': 'FOUR', 'five': 'FIVE'}
  >>> merge2 = dict1 | dict2 # Very Pythonic
  >>> merge2
  {'one': 1, 'two': 'TWO', 'three': 3, 'four': 'FOUR', 'five': 'FIVE'}
  >>> merge3 = dict2 | dict1
  # value of key `two` is different now
  >>> merge3
  {'four': 'FOUR', 'two': 2, 'five': 'FIVE', 'one': 1, 'three': 3} 
  >>>
  ```

- Exercise 4.4.3.1

  ``` Python
  user = {
  ...     "username": "John Doe",
  ...     "password": "secret",
  ...     "password_confirmation": "secret"
  ... }
  >>> if (user["password"] == user["password_confirmation"]):
  ...     print(f"The settings for {user["username"]} are correct")
  ... else:
  ...     print(f"The settings for {user["username"]} not are correct")
  ...     
  The settings for John Doe are correct
  >>>
  ```

### Applying `enumerate()` to `dict.items()`

- Exercise 4.4.3.2

- It's possible to apply [`enumerate()`](https://docs.python.org/3/library/functions.html#enumerate) *fn* to [`dict.items()`](#dictitems)

  ``` Python
  >>> for i, (name, year) in enumerate(moonwalks.items()):
  ...     print(f"{i+1}. {name} first performed a moonwalk in {year}")
  ...     
  1. Neil Armstrong first performed a moonwalk in 1969 
  2. Buzz Aldrin first performed a moonwalk in 1969    
  3. Alan Shepard first performed a moonwalk in 1971   
  4. Eugene Cernan first performed a moonwalk in 1972  
  5. Michael Jackson first performed a moonwalk in 1983
  >>>
  ```

- Exercise 4.4.3.2 see [above](#442-merging-dictionaries)
