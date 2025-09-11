# 5. Functions and Iterators

- [5. Functions and Iterators](#5-functions-and-iterators)
  - [Function Definitions](#function-definitions)

## Function Definitions

- continued see [hartl](../README.md#hartl) p.120

- In Python, functions can be defined using the [**`def`**](https://docs.python.org/3/reference/compound_stmts.html#function-definitions) *keyword*.

  ``` Python
  >>> def square(number):
  ...     return number * number
  ...     
  >>> square(2)
  4

  >>> def squares_list(n):
  ...     result = []
  ...     for i in range(n + 1):
  ...         result.append(i ** 2)
  ...     return result
  ...     
  >>> squares_list(10)
  [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
  ```

- The function ends with the **`return`** *keyword* followed by the *return value* for the function. As soon as Python sees an occurrence of `return` it leaves the *function* entirely.

  ``` Python
  >>> def first_greater_than_max(max, numbers):
  ...     for n in numbers:
  ...         if n > max:
  ...             return n
  ...     return None
  ...     
  >>> first_greater_than_max(5, [2, 4, 6, 8])
  6   
  >>> first_greater_than_max(1, [2, 4, 6, 8])
  2
  >>> first_greater_than_max(7, [2, 4, 6, 8])
  8
  >>> first_greater_than_max(9, [2, 4, 6, 8])
  >>> print(first_greater_than_max(9, [2, 4, 6, 8]))
  None
  ```

- ☝ **Returning `None` ist the default!**

  ``` Python
  >>> def first_greater_than_max2(max, numbers):
  ...     for n in numbers:
  ...         if n > max:
  ...             return n
  ... 
  >>> print(first_greater_than_max2(9, [2, 4, 6, 8]))
  None
  ```

- Example `day_name()`

  ``` Python
   >>> from datetime import datetime
  >>> now = datetime.now()
  >>> type(now)
  <class 'datetime.datetime'>
  >>> now.weekday()
  3   
  >>> import calendar
  >>> calendar.day_name
  <calendar._localized_day object at 0x0000013A88991010>
  >>> list(calendar.day_name)
  ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  >>> calendar.day_name[now.weekday()]
  'Thursday'
  >>> def day_name(datetime):
  ...     """ Return the name of the day of the week for the passed `datetime`"""
  ...     return calendar.day_name[datetime.weekday()]
  ... 
  >>> day_name(now)
  'Thursday'
  ```
