# 5. Functions and Iterators

- [5. Functions and Iterators](#5-functions-and-iterators)
  - [5.1 Function Definitions](#51-function-definitions)
    - [*docstring* and `help()` *fn*](#docstring-and-help-fn)
    - [5.1.1 First Class Functions](#511-first-class-functions)
      - [Assign functions to variables](#assign-functions-to-variables)
      - [Pass a function as arguments to a function](#pass-a-function-as-arguments-to-a-function)
      - [A function can return a function](#a-function-can-return-a-function)
    - [5.1.2 Variable and Keyword Arguments](#512-variable-and-keyword-arguments)
      - [star args - `*args`](#star-args---args)
      - [star star kwargs - **`**kwargs`**](#star-star-kwargs---kwargs)
  - [5.2 Functions in a file](#52-functions-in-a-file)

## 5.1 Function Definitions

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

### *docstring* and `help()` *fn*

- A **docstring** follows immediately after the *`def`* keyword, the *function name* and any *arguments*.  

- The *docstring* typically use the imperative mood, so  
  … *"Return the name"* rather than *"Returns the name"*.

- The *docstring* is shown via the [**`help()`**](https://docs.python.org/3/library/functions.html#help) *fn*

  ``` Python
  >>> import calendar
  >>> from datetime import datetime
  >>> def day_name(datetime):
  ...     """ Return the name of the day of the week for the passed `datetime`"""
  ...     return calendar.day_name[datetime.weekday()]
  ...     
  >>> help(day_name)
  Help on function day_name in module __main__:

  day_name(datetime)
      Return the name of the day of the week for the passed `datetime`

  >>>
  ```

- Then, there's a *function body*, which determines the *return value* of the function using the *`return`* keyword.

- Finally, the function is **ended by a *newline***.

### 5.1.1 First Class Functions

- continued see [hartl](../README.md#hartl) p.126

- Python *functions* **can be treated as regular variables** in many ways (*first-class objects*).

#### Assign functions to variables

- We can assign a function to a variable and are able to call it via the variable

  ``` Python
  >>> def square(x):
  ...     return x * x
  ... 
  >>> pow2 = square
  >>> pow2(4)
  16
  ```

#### Pass a function as arguments to a function

- We can pass functions as arguments to other functions.

  ``` Python
  >>> def inc(x, f):
  ...     return f(x) + 1
  ...     
  >>> inc(4, square)
  17
  >>> inc(4, pow2)
  17
  ```

#### A function can return a function

- A function can return another function

  ``` Python
  >>> def inc_by_1(x):
  ...     return x + 1
  ...     
  >>> def inc_by_2(x):
  ...     return x + 2
  ...     
  >>> def inc_by_4(x):
  ...     return x + 4
  ...     
  >>> def incer(y):
  ...     if (y == 4): return inc_by_4
  ...     elif (y == 2): return inc_by_2
  ...     else: return inc_by_1
  ...     
  >>> print(incer(1)(42))
  43  
  >>> print(incer(2)(42))
  44  
  >>> print(incer(4)(42))
  46
  ```

### 5.1.2 Variable and Keyword Arguments

- continued see [hartl](../README.md#hartl) p.128

#### star args - `*args`

- Passing a variable number of arguments via `*args`

  ``` Python
  >>> def bar(*args):
  ...     print(args)
  ...     return type(args)
  ... 
  >>> bar ("This", "is", "the", "end")
  ('This', 'is', 'the', 'end')
  <class 'tuple'>
  >>> 
  ```

  Python creates a *tuple* of the arguments automatically,  
  ... which works for any number.

#### star star kwargs - **`**kwargs`**

- Passing a variable number of *key-value* pairs as arguments via `**kwargs`

  ``` Python
  >>> def foo(**kwargs):
  ...     print(kwargs)
  ...     return type(kwargs)
  ... 
  >>> foo(a='One', b='Two', c='Three')
  {'a': 'One', 'b': 'Two', 'c': 'Three'}
  <class 'dict'>
  >>> foo(one='1', two='2', three='3')
  {'one': '1', 'two': '2', 'three': '3'}
  <class 'dict'>
  >>> foo(1='1', 2='2', 3='3')
    File "<stdin>", line 1
      foo(1='1', 2='2', 3='3')
  SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
  ```

- Python creates a *dictionary* of the passed *key-value* pairs.

- Example 5.1.3.2

  ``` Python
  >>> def deriver(f, x):
  ...     h = 0.00001
  ...     return (f(x+h) - f(x))/h
  ... 
  >>> def square(x):
  ...     return x*x
  ... 
  >>> deriver(square, 3)
  6.000009999951316
  >>> 
  ```

- Example 5.1.3.3

  ``` Python
  >>> def foo(*args, **kwargs):
  ...     print(args)
  ...     print(kwargs)
  ... 
  >>> foo("This" "is a bunch", "of arguments", "to the function", a="hello", b="world", bar="good day!")
  ('Thisis a bunch', 'of arguments', 'to the function')
  {'a': 'hello', 'b': 'world', 'bar': 'good day!'}
  ```

## 5.2 Functions in a file

- continued see [hartl](../README.md#hartl) p.130

- Since `-` (*hyphen*) seems to be problematic in import paths, I renamed the chapter folder.

- Usually, we put the function definitions in a separate file.

- Using such an *external resource* requires the presence of a file called **`__init__.py`**,  
  … which causes Python to interpret our project directory as a **package**.  
  … The file doesn’t have to have any content, though—it just has to exist.

- We have to **`import`** the *function* the same way that we imported `datetime`, and `calendar`

  ``` Python
  # chp005_functions_iterators/package/p005_01_day.py
  from datetime import datetime
  from calendar import day_name

  def dayname(time):
      """Return the name of the day in a week."""
      return day_name[time.weekday()]
  ```

  ``` Python
  # chp005_functions_iterators/p005.01.greet.py
  # user@ideapad:~/home_rus/learn-python-01/chp005_functions_iterators$ python3 ./p005.01.greet.py 

  from datetime import datetime

  from package.p005_01_day import dayname


  print(f"Today is {dayname(datetime.now())}")
  ```
  
- Note that the `import` statement includes the current directory (`package`), which is necessary because our *project directory* **isn’t** on the *Python include path by default*.

- In the book example, the imports from the *standard library* (`datetime`) come first, then we import a *third-party library* (`flask`), and finally the import of the custom library follows.

- By convention each section is separated by  a *newline* and from the rest of the file by *two newlines*.
