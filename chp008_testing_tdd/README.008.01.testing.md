# 8. Testing and Test-Driven Development

- TODO TOC

- As it turns out,  
  … learning how to write (automatic) Python tests will also give us a chance  
  … to learn how to create (and publish!) a Python package.

- Here’s our strategy for testing the current palindrome code and extending it to more complicated phrases:

  1. Set up our initial package.

  2. Write automated tests for the existing `ispalindrome()` functionality.

  3. Write a **failing test** for the enhanced palindrome detector (*RED*).

  4. Write (possibly ugly) code to get the test passing (*GREEN*).

  5. Refactor the code to make it prettier, while ensuring that the test suite stays *GREEN*.

## 8.1 Package Setup

- continued see [hartl](../README.md#hartl) p.192

- In this section we’ll create a package based on the palindrome detector.  
  see [hartl](../README.md#hartl) p.193-195

- With all that configuration done, we’re now ready to configure the environment
for development and testing.  
  
  … As in Section 1.3, we’ll use `venv` for the virtual environment.  
  … Instead of use `venv`, I will use `pyenv`!  
  
  … We’ll also be using `pytest` for testing, which we can install using `pip`.  
  … I upgraded `pip`, as described in the book,  
  … and installed the highest available version `7` of `pytest`.

  ``` bash
  …/learn_python_01_package_008_tutorial> pyenv local 3.13
  …/learn_python_01_package_008_tutorial> python3 --version
  Python 3.13.7
  # Successfully upgrade pip from 'pip-25.2' to 'pip-25.3'
  …/learn_python_01_package_008_tutorial> pip install --upgrade pip
  …/learn_python_01_package_008_tutorial> pip index versions pytest
  pytest (8.4.2)
  Available versions: 8.4.2, 8.4.1, 8.4.0, 8.3.5, 8.3.4, 8.3.3, 8.3.2, 8.3.1, 8.3.0, 8.2.2, 8.2.1, 8.2.0, 8.1.2, 8.1.1, 8.0.2, 8.0.1, 8.0.0, 7.4.4, …
  …/learn_python_01_package_008_tutorial> pip install pytest==7.4.4
  ```
