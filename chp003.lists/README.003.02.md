# 3. Lists

TODO TOC

- see [hartl](../README.md#hartl) p.74

## 3.3 List Slicing

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
