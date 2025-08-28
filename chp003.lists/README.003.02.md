# 3. Lists

- [3. Lists](#3-lists)
  - [3.3 List Slicing](#33-list-slicing)
    - [`slice()` function](#slice-function)
    - [Slicing using extended index syntax](#slicing-using-extended-index-syntax)
  - [3.4 More List Techniques](#34-more-list-techniques)
    - [3.4.1 Element Inclusion](#341-element-inclusion)
    - [3.4.2 Sorting, Reversing, and Comparison](#342-sorting-reversing-and-comparison)
      - [`.sort()` and `.reverse()` methods](#sort-and-reverse-methods)
      - [Copy a list with `list()` *fn* and create a reveres list with `reversed()` *fn*](#copy-a-list-with-list-fn-and-create-a-reveres-list-with-reversed-fn)
      - [Creating a sorted list with `sorted()` *fn*](#creating-a-sorted-list-with-sorted-fn)
      - [Comparison](#comparison)
        - [Equality and Inequality](#equality-and-inequality)
        - [`is` tests if its the **same object**](#is-tests-if-its-the-same-object)
        - [PEP 8: When comparing with `None` use always `is`](#pep-8-when-comparing-with-none-use-always-is)
    - [3.4.3 Appending and Popping](#343-appending-and-popping)
    - [3.4.4 Undoing a `Split` - `Join`](#344-undoing-a-split---join)

## 3.3 List Slicing

- continued see [hartl](../README.md#hartl) p.75

- *Slicing* allows to access multiple elements at a time.

### `slice()` function

- Use the [`slice()`](https://docs.python.org/3/library/functions.html#slice) function and provide two arguments corresponding to the set of indices where the slice should starts and ends **specified by [`range()`](https://docs.python.org/3/library/functions.html#func-range)**.

  ``` Python
  >>> list(range(1,3))
  [1, 2]
  >>> a = [42, 8, 17, 99]
  >>> a[slice(1,3)] # NOT Pythonic
  [8, 17]
  >>> a[slice(2,3)] # NOT Pythonic
  [17]
  ```

### Slicing using extended index syntax

- see <https://python-reference.readthedocs.io/en/latest/docs/brackets/slicing.html>

  ``` Python
  >>> a = [42, 8, 17, 99]
  >>> a[1:3] # # a[start:-end]; Pythonic
  [8, 17]
  >>> a[:3]
  [42, 8, 17]
  >>> a[1:]
  [8, 17, 99]
  >>> a[1:3:2] # a[start:end:step]
  [8]
  >>> a[1::2]
  [8, 99]
  >>> a[:-2:2] # a[start:-end:step]
  [42]
  >>> a[:-2]
  [42, 8]
  >>> a[::-1] # a[::-step]
  [99, 17, 8, 42]

  # Further examples
  >>> zero2nine = list(range(0,10))
  >>> zero2nine
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  >>> zero2nine[0:6]
  [0, 1, 2, 3, 4, 5]
  >>> zero2nine[0:6:-1] # ☝NOTE!
  []
  >>> zero2nine[0:6][::-1] # ☝NOTE!
  [5, 4, 3, 2, 1, 0]
  >>> zero2nine[0:6:2]
  [0, 2, 4]
  >>> zero2nine[1:6:2]
  [1, 3, 5]  
  ```

- Exercise 3.3.1 - Slicing with *strings* and *lists*

  ``` Python
  >>> zero2nine = list(range(0, 10))
  >>> zero2nine[3:len(zero2nine)-2]
  [3, 4, 5, 6, 7]
  >>>
  >>> animals = "ant bat cat"
  >>> animals[3:7]
  ' bat'
  >>> animals[4:7]
  'bat'
  >>>   
  ```

## 3.4 More List Techniques

- see [hartl](../README.md#hartl) p.77

### 3.4.1 Element Inclusion

- As with [*strings*](../chp002.strings//README.002.03.md#find-method-and-in-operator), *lists* support testing for element inclusion using the [`in`](https://python-reference.readthedocs.io/en/latest/docs/operators/in.html) operator:
  
  ``` Python
  # `in` with strings
  >>> animals = "ant bat cat"
  >>> 'dog' in animals
  False
  >>> 'bat' in animals
  True
  # `in` with strings
  >>> animals = animals.split()
  >>> animals
  ['ant', 'bat', 'cat']
  >>> 'bat' in animals
  True
  >>> 'dog' in animals
  False
  ```

### 3.4.2 Sorting, Reversing, and Comparison

- *Sorting* and *reversing* list come in two general types:
  - *in-place* and
  - *generators*

#### `.sort()` and `.reverse()` methods

- see <https://docs.python.org/3/tutorial/datastructures.html#more-on-lists>

- `.sort()` and `.reverse()` **mutate** the original list:

  ``` Python
  >>> # `.reverse()`
  >>> animals = animals.split()
  >>> animals
  ['ant', 'bat', 'cat']
  >>> animals.reverse()
  >>> animals
  ['cat', 'bat', 'ant']
  >>> # `.sort()` with a list of strings
  >>> numbers = ["1", "11", "2", "23", "3", "31"]
  >>> numbers
  ['1', '11', '2', '23', '3', '31']
  >>> numbers.sort()
  >>> numbers
  ['1', '11', '2', '23', '3', '31']
  >>> # `.sort()` with a list of numbers
  >>> numbers = [1, 11, 2, 23, 3, 31]
  >>> numbers
  [1, 11, 2, 23, 3, 31]
  >>> numbers.sort()
  >>> numbers
  [1, 2, 3, 11, 23, 31]

#### `.copy()`

- see <https://docs.python.org/3/tutorial/datastructures.html#more-on-lists>

- `.copy()` returns a **shallow copy** of a *list*

  ``` Python
  # `.copy()`
  >>> origin = ["ant", "bat", "cat"]
  >>> alias = origin
  >>> alias.reverse()
  >>> origin
  ['cat', 'bat', 'ant']
  >>> copy = origin.copy()
  >>> copy
  ['cat', 'bat', 'ant']
  >>> copy.reverse()
  >>> copy
  ['ant', 'bat', 'cat']
  # ☝ `origin` is unchanged!
  >>> origin
  ['cat', 'bat', 'ant']
  ```

#### Copy a list with `list()` *fn* and create a reveres list with `reversed()` *fn*

- see <https://docs.python.org/3/library/functions.html#reversed>
  
  ``` Python
  >>> origin = ["ant", "bat", "cat"]
  >>> anotherCopy = list(origin)
  # `reversed()` returns an iterator; 
  # to create a list from the iterator call `list()`
  >>> anotherCopyReversed = list(reversed(anotherCopy))
  >>> anotherCopy = anotherCopy[1:3]
  >>> anotherCopy
  ['bat', 'cat']
  >>> anotherCopyReversed
  ['cat', 'bat', 'ant']
  >>> origin
  ['ant', 'bat', 'cat']
  ```

#### Creating a sorted list with `sorted()` *fn*

- see <https://docs.python.org/3/library/functions.html#sorted>

  ``` Python
  >>> anotherCopyReversed
  ['cat', 'bat', 'ant']
  >>> origin
  ['ant', 'bat', 'cat']
  # `sorted()` returns a list and not an iterator like `reversed()`
  >>> sorted(anotherCopyReversed)
  ['ant', 'bat', 'cat']
  ```

#### Comparison

##### Equality and Inequality

- see [hartl](../README.md#hartl) p.79

- Lists support some basic equality and inequality comparisons like strings:

  ``` Python
  >>> a = [1, 2, 3]
  >>> b = [1, 2, 3]
  >>> a == b
  True
  >>> a != b
  False
  >>>
  ```

##### `is` tests if its the **same object**

- Python also supports [`is`](https://docs.python.org/3/library/operator.html#operator.is_) which tests **object identity**.

  ``` Python
  # …
  >>> c = a
  >>> a is b
  False
  >>> a is c
  True
  ```

##### PEP 8: When comparing with `None` use always `is`

- According to [PEP 8](https://peps.python.org/pep-0008/#programming-recommendations)  
  > Comparisons to singletons like `None` should always be done with **`is`** or **`is not`**,  
  … **NEVER** the *equality operators*.

- The [`None`](https://docs.python.org/3/c-api/none.html) object is a *singleton* and denotes **lack of value**.

  ``` Python
  >>> a = [3, 2, 1]
  >>> a is None # ☝ Pythonic
  False
  >>> a.sort() is None
  True
  >>> a
  [1, 2, 3]
  >>> a.reverse() == None # ☝ NOT Pythonic
  True
  >>> a
  [3, 2, 1]
  ```

### 3.4.3 Appending and Popping

- see [hartl](../README.md#hartl) p.79

- Append and remove elements to the end of a list with the Methods [`.append()`](https://docs.python.org/3/tutorial/datastructures.html#data-structures) and [`pop()`](https://docs.python.org/3/tutorial/datastructures.html#data-structures):

- Note:  
  … `.pop()` returns the value of the final element or the value at the specified index while **removing** it as a side effect.
  … `.appends()` add an element to the end of the list and returns `None`.

  ``` Python
  >>> a = sorted([9, 1, 3])
  >>> a
  [1, 3, 9]
  >>> a.append(42)
  >>> a
  [1, 3, 9, 42]
  >>> a.append(True)
  >>> a
  [1, 3, 9, 42, True]
  >>> a. append("Foo")
  >>> a
  [1, 3, 9, 42, True, 'Foo']
  >>> foo = a.pop()
  >>> foo
  'Foo'
  >>> a.append(foo) is None
  True
  >>> fourtytwo = a.pop(3)
  >>> fourtytwo
  42  
  >>> a
  [1, 3, 9, True, 'Foo']
  >>> 
  >>> a.pop(42)
  Traceback (most recent call last):
    File "<python-input-46>", line 1, in <module>
      a.pop(42)
      ~~~~~^^^^
  IndexError: pop index out of range
  ```

### 3.4.4 Undoing a `Split` - `Join`

- see [hartl](../README.md#hartl) p.79

- Using a **generator expression** that returns `str(e)` for each element in the list

  ``` Python
  >>> a = "To be or not to be".split() # splits the string into a list of strings
  >>> a
  ['To', 'be', 'or', 'not', 'to', 'be']
  >>> "".join(a) # joins the string elements of a list to a string
  'Tobeornottobe'
  >>> " ".join(a) # the string providing this method serves as separator
  'To be or not to be'
  >>> a.insert(3, 42) # inserts an element at index
  >>> a
  ['To', 'be', 'or', 42, 'not', 'to', 'be']
  >>> " ".join(a) # str.join expects only strings
  Traceback (most recent call last):
    File "<python-input-18>", line 1, in <module>
      " ".join(a)
      ~~~~~~~~^^^
  TypeError: sequence item 3: expected str instance, int found
  # ☝ Using a generator expression that returns str(e) for each element in the list
  >>> " ".join(str(e) for e in a)
  'To be or 42 not to be'  
  ```

- Exercise 3.4.5

  - 1. `list.sort(reverse=True)` and `sorted(reverse=True)`

  ``` Python
  >>> a = [9, 5, 7, 1, 3]
  >>> a1 = a.copy()
  >>> a1.sort(reverse=True)
  >>> a1
  [9, 7, 5, 3, 1]
  >>> a2 = a.copy()
  >>> sorted(a, reverse=True)
  [9, 7, 5, 3, 1]
  ```

  - 1. `list.insert(i, x)`

  ``` Python
  >>> a2.insert(0, 11)
  >>> a2
  [11, 9, 5, 7, 1, 3]
  ```

  - 1. `list.extend(iterable)`

  ``` Python
  >>> a = ['a', 'b', 'c']
  >>> b = ['d', 'e', 'f']
  >>> a1 = a.copy()
  >>> a1.extend(b)
  >>> a1
  ['a', 'b', 'c', 'd', 'e', 'f'] # a1 was mutated
  >>> a
  ['a', 'b', 'c']
  >>> b
  ['d', 'e', 'f']
  >>> a2 = a.copy()
  >>> a2[len(a2):] = b  # a2 was mutated
  >>> a2 
  ['a', 'b', 'c', 'd', 'e', 'f']
  >>> 
  ```
