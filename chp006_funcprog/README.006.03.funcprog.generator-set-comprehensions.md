# 6. Functional Programming

- [6. Functional Programming](#6-functional-programming)
  - [6.4 Generator and Set Comprehensions](#64-generator-and-set-comprehensions)
    - [6.4.1 Generator Comprehensions](#641-generator-comprehensions)
    - [6.4.2 Set Comprehensions](#642-set-comprehensions)

## 6.4 Generator and Set Comprehensions

- continued see [hartl](../README.md#hartl) p.163

### 6.4.1 Generator Comprehensions

- Remember from section [5.3.1 Generators](../chp005_functions_iterators/README.005.03.generators.md#531-generators)

  ``` Python
  >>> set("0123456789")
  {'1', '8', '3', '4', '6', '5', '2', '0', '7', '9'}

  >>> def first_all_digits(numbers):
  ...   for n in numbers:
  ...     if (set(str(n)) == set("0123456789")):
  ...       return n
  ...   return None
  ... 
  ```

- Then we tried to use an *imperative squares generator* without using a *generator*,  
  … but this would take to long since we produce the whole list before.

  The following snippet shows an *functional* approach for this leveraging *list comprehension*:

  ``` Python
  # list comprehension but still takes too long
  >>> squares = [n**2 for n in range(10**8 + 1)] 
  ^CTraceback (most recent call last):
    File "<stdin>", line 1, in <module>
      import platform
                ^^^^
  KeyboardInterrupt # Ctrl + C pressed
  ```

- Then we used an **generator** to create square numbers,  
  … but the generator was implemented in an *imperative style*.

  ``` Python
  >>> def imperative_squares_generator():
  ...   for n in range(10**8 + 1):
  ...     yield n**2
  ... 

  >>> first_all_digits(imperative_squares_generator())
  1026753849
  ```

- Here comes the *functional* approach using a **generator comprehension**

  ``` Python
  >>> def functional_squares_generator():
  ...   return (n**2 for n in range(10**8 + 1))
  ... 
  >>> first_all_digits(functional_squares_generator())
  1026753849
  >>> 
  ```

  The *generator comprehension*, which **looks just like** a *list comprehension*  
  … **except with parentheses** instead of *square brackets*.  

  As with the *imperative generator* above, this supplies the next number **only when required**.

### 6.4.2 Set Comprehensions

- The syntax of **set comprehensions** (both without and with *conditions*)  
  … is nearly identical to the syntax for *list comprehensions*  
  … just with **curly braces** in place of *square brackets*.

  ``` Python
  >>> {n for n in range(5, 11)}
  {5, 6, 7, 8, 9, 10}
  >>> {n for n in range(5, 11) if n % 2 ==0}
  {8, 10, 6}
  >>> {n for n in range(5, 11) if n % 2 ==0} | {n for n in range(5,11) if n % 2 !=0}
  {5, 6, 7, 8, 9, 10}
  ```

- Exercise 6.4.3

  ``` Python
  >>> count = 10
  >>> (n * 2 for n in range(1, count + 1))
  <generator object <genexpr> at 0x7f6afca40e10>
  >>> generator = (n * 2 for n in range(1, count + 1))
  >>> list(generator)
  [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
  ```
