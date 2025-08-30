# 3. Lists

- [3. Lists](#3-lists)
  - [3.6 Tuples and Sets](#36-tuples-and-sets)
    - [Tuples](#tuples)
      - [Tuple declaration](#tuple-declaration)
      - [Tuple iteration](#tuple-iteration)
      - [Tuple slicing](#tuple-slicing)
      - [Tuple or List unpacking](#tuple-or-list-unpacking)
      - [Literal Single element tuple - an object in parentheses alone is just the object itself](#literal-single-element-tuple---an-object-in-parentheses-alone-is-just-the-object-itself)
    - [Sets](#sets)
      - [Set declaration](#set-declaration)
      - [Union and Intersection](#union-and-intersection)
      - [Set elements cannot be accessed directly - but can be tested for inclusion and iterated](#set-elements-cannot-be-accessed-directly---but-can-be-tested-for-inclusion-and-iterated)
    - [Empty lists, tuples or sets are `False` in a boolean context](#empty-lists-tuples-or-sets-are-false-in-a-boolean-context)
      - [`type()` function](#type-function)
    - [`tuple()` function](#tuple-function)
    - [`.pop()` and `.add()` for sets](#pop-and-add-for-sets)

## 3.6 Tuples and Sets

- continued see [hartl](../README.md#hartl) p.86

### Tuples

- tuples are basically lists that can't be changed – tuples are **immutable**!

#### Tuple declaration

- **Literal tuples** can be created in much the same way as *literal lists*.  
  … The **only difference** is that tuples use *parentheses* **instead of** *square brackets*.

  ``` Python
  >>> a = ["ant", "bear", "spider"] # Literal list
  >>> a[1] = "dog"
  >>> a
  ['ant', 'dog', 'spider']
  >>> t = ("ant", "bear", "spider") # Literal tuple
  >>> t[1] = "dog"
  Traceback (most recent call last):
    File "<python-input-5>", line 1, in <module>
      t[1] = "dog"
      ~^^^
  TypeError: 'tuple' object does not support item assignment
  >>> t.sort()
  Traceback (most recent call last):
    File "<python-input-8>", line 1, in <module>
      t.sort()
      ^^^^^^
  AttributeError: 'tuple' object has no attribute 'sort'
  >>> t.append("goose")
  Traceback (most recent call last):
    File "<python-input-9>", line 1, in <module>
      t.append("goose")
      ^^^^^^^^
  AttributeError: 'tuple' object has no attribute 'append'  
  ```

#### Tuple iteration

- Iterating over a tuple with the `for in` loop

  ``` Python
  >>> t = ("ant", "bear", "spider") # Literal tuple
  >>> for e in t:
  ...     print(e)
  ... 
  ant
  bear
  spider
  ```

#### Tuple slicing

- tuples support *slicing*

  ``` Python
  >>> t = ("spider", "eagle", "bear", "ant")
  >>> t
  ('spider', 'eagle', 'bear', 'ant')
  >>> t1 = t[1:3]
  >>> t1
  ('eagle', 'bear')
  ```

- Some functions also accept tuples as **arguments** where lists are  possible.

  ``` Python
  >>> t = ("spider", "eagle", "bear", "ant") # a tuple
  >>> t
  ('spider', 'eagle', 'bear', 'ant')
  >>> l2 = sorted(t)                         # sorted returns a list 
  >>> l2
  ['ant', 'bear', 'eagle', 'spider']         # a list
  ```

#### Tuple or List unpacking

- Parentheses can be omitted when defining literal tuples – **NOT RECOMMENDED** for *declaring tuples*
  
  ``` Python
  >>> t2 = 2, 4, 6, 8
  >>> t2
  (2, 4, 6, 8)
  >>> t3 = (2, 4, 6, 8)
  >>> t3
  (2, 4, 6, 8)
  >>> t2 == t3
  True
  >>> t4 = 1, 3, 5, 7, 9
  >>> t4
  (1, 3, 5, 7, 9)
  >>> t4 == t3
  False  
  ```

- **Multiple** *assignments* at on **once** – list or tuple **unpacking**  
  … Pythonic use case for *parentheses-less* tuple notation

  ``` Python
  >>> t = ("ant", "bear", "eagle")
  >>> ant, bear, eagle = t # tuple unpacking; Very Pythonic
  >>> ant
  'ant'
  >>> bear
  'bear'
  >>> eagle
  'eagle'
  >>> 
  >>> (ant2, bear2, eagle2) = t # Alternatively with parentheses
  >>> ant2
  'ant'
  >>> bear2
  'bear'
  >>> eagle2
  'eagle'  
  >>> 
  >>> l = ["antl", "bearl", "eaglel"]
  >>> ant, bear, eagle = l # list unpacking; Very Pythonic
  >>> ant
  'antl'
  >>> bear
  'bearl'
  >>> eagle
  'eaglel'
  ```

- You can also use the parentheses-less notification, to show the variables values

  ``` Python
  # …
  >>> ant, eagle, bear
  ('antl', 'eaglel', 'bearl')
  ```

#### Literal Single element tuple - an object in parentheses alone is just the object itself

- continued see [hartl](../README.md#hartl) p.88

- Defining a *tuple of one element* requires a **☝ trailing comma**  
  … because **☝ an object in parentheses alone is just the object itself**.

  ``` Python
  >>> ("ant")
  'ant'
  >>> ("ant",)
  ('ant',)
  >>> "".join(reversed(("ant")))
  'tna'
  >>> "".join(reversed(("ant",)))
  'ant'
  ```

### Sets

- Correspond closely to the *mathematical definition* and can be thought of as lists of elements where
  - repeat values are ignored and
  - the order doesn't matter.

#### Set declaration

- Sets can be initialized literally using curly braces or
  … by passing an *iterable* to the [**`set()`**](https://docs.python.org/3/library/functions.html#func-set) *fn*

  ``` Python
  >>> s = {1, 2, 3, 3, 4, 1}
  >>> s
  {1, 2, 3, 4}
  >>> s2 = s.copy()
  >>> s2
  {1, 2, 3, 4}
  >>> s2 = {4, 3, 2, 1}
  >>> s2
  {1, 2, 3, 4}
  >>> s == s2
  True
  >>> s3 = set([1, 1, 2, 2, 3, 3, 4, 4])
  >>> s3
  {1, 2, 3, 4}
  >>> s == s3
  True
  >>> s4 = set((1, 1, 2, 2, 3, 3, 4, 4))
  >>> s4
  {1, 2, 3, 4}
  >>> s == s4
  True
  ```

#### Union and Intersection

- Sets provides support for many common set operations

  ``` Python
  >>> s1 = {"ant", 42, "bat"}
  >>> s2 = {42, "bat", 666}
  >>> s1 | s2 # Union
  {'bat', 666, 42, 'ant'}
  >>> s1 & s2 # Intersection
  {'bat', 42}
  >>>    
  ```

#### Set elements cannot be accessed directly - but can be tested for inclusion and iterated

- Iteration and test for inclusion

  ``` Python
  >>> s1 = {"ant", 42, "bat"}
  # direct access is not supported
  >>> s1[1]
  Traceback (most recent call last):
    File "<python-input-79>", line 1, in <module>
      s1[1]
      ~~^^^
  TypeError: 'set' object is not subscriptable   
  # unpacking assignment seems to work
  >>> a1, a2 = s1
  Traceback (most recent call last):
    File "<python-input-82>", line 1, in <module>   
      a1, a2 = s1
      ^^^^^^
  ValueError: too many values to unpack (expected 2)
  >>> a1, a2, a3 = s1
  >>> a1
  'bat'
  >>> a2
  42  
  >>> a3
  'ant'
  # testing
  >>> "ant" in s1
  True
  >>> 666 in s1
  False
  # Iteration
  >>> for e in s1:
  ...     print(e)
  ... 
  bat
  42
  ant
  >>> 
  ```

### Empty lists, tuples or sets are `False` in a boolean context

#### `type()` function

- see [**`type()`**](https://docs.python.org/3/library/functions.html#type)

- An empty list, tuple or set are `False` in a boolean context

  ``` Python
  >>> type([])
  <class 'list'>
  >>> type(())
  <class 'tuple'>
  # ☝ We CAN'T use `{}` to declare an empty set; returns an empty dictionary
  >>> type({})
  <class 'dict'> 
  # ☝ … instead, we CAN use `set()`dictionary
  >>> type(set())
  <class 'set'>
  >>> bool(set())
  False
  >>> bool([])
  False
  >>> bool(())
  False
  ```

- Exercise 3.6.1

### `tuple()` function

- see [`tuple()`](https://docs.python.org/3/library/functions.html#func-tuple);  
  … `tuple()` is actually an immutable sequence type, rather than a function.

  ``` Python
  >>> t = (2, 4, 6)
  >>> type(t)
  <class 'tuple'>
  >>> l = sorted(t)
  >>> t = (4, 6, 2)
  >>> type(t)
  <class 'tuple'>
  >>> l = sorted(t)
  >>> l
  [2, 4, 6]
  >>> t = tuple(l)
  >>> t
  (2, 4, 6)
  >>> type(t)
  <class 'tuple'>
  ```

### `.pop()` and `.add()` for sets

- see [`.pop()`](https://docs.python.org/3/library/stdtypes.html#frozenset.pop) and [`.add()`](https://docs.python.org/3/library/stdtypes.html#frozenset.add)

  ``` Python
  >>> s = set(range(0,5))
  >>> s
  {0, 1, 2, 3, 4}
  >>> last = s.pop()
  >>> last
  0   
  >>> s
  {1, 2, 3, 4}
  >>> last = s.pop()
  >>> s
  {2, 3, 4}
  >>> s.append(5) # No `.append()` but a `.add()` method
  Traceback (most recent call last):
    File "<python-input-115>", line 1, in <module>      
      s.append(5)
      ^^^^^^^^
  AttributeError: 'set' object has no attribute 'append'
  >>> s.add(5)
  >>> s
  {2, 3, 4, 5}
  ```
