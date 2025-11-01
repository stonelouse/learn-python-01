# 8. Testing and Test-Driven Development

- [8. Testing and Test-Driven Development](#8-testing-and-test-driven-development)
  - [8.1 Package Setup](#81-package-setup)
  - [8.2 Initial Test Coverage](#82-initial-test-coverage)
    - [8.2.1 A Useful Passing Test](#821-a-useful-passing-test)
    - [8.2.2 Pending Tests - `skip()`](#822-pending-tests---skip)

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

## 8.2 Initial Test Coverage

- see [hartl](../README.md#hartl) p.198

- Now that we’ve set up our basic package structure, we’re ready to get started testing.

  ``` bash
  …/learn_python_01_package_008_tutorial> pytest
  ================================ test session starts ================================
  platform linux -- Python 3.13.7, pytest-7.4.4, pluggy-1.6.0
  rootdir: /mnt/ntfs1/home.UserRus/Documents.Notes/learn_python_01_package_008_tutorial
  collected 0 items                                                                                                                                                                   

  =============================== no tests ran in 0.02s ===============================
  ```

- Now let’s write a minimal failing test - make it *RED*.
  
  ``` Python
  # tests/test_phrase.py
  def test_initial_example():
    assert False
  ```
  
  see `…/learn_python_01_package_008_tutorial/tests/test_phrase.py`  
  … commit `946df15a5dde31f0d7982e107b27ca048f8a8939`

  We define a function containing one **assertion**,  
  … which *asserts* that something has a boolean value of `True`,  
  … in which case the *assertion* **passes**,  
  … and **fails** *otherwise*.

  Because the code above *asserts* that `False` is `True`, it **fails** by design:

  ``` bash
  …/learn_python_01_package_008_tutorial> pytest
  ================================ test session starts ================================
  platform linux -- Python 3.13.7, pytest-7.4.4, pluggy-1.6.0
  rootdir: /mnt/ntfs1/home.UserRus/Documents.Notes/learn_python_01_package_008_tutorial
  collected 1 item                                                                                                                                                                    

  tests/test_phrase.py F                                                         [100%]

  ===================================== FAILURES ======================================
  _______________________________ test_initial_example ________________________________

      def test_initial_example():
  >       assert False
  E       assert False

  tests/test_phrase.py:2: AssertionError
  ============================== short test summary info ==============================
  FAILED tests/test_phrase.py::test_initial_example - assert False
  ================================= 1 failed in 0.60s =================================
  ```

  This test is not useful, but it *demonstrates the concept*.

- Now let's pass the test - make it *GREEN*.
  
  ``` Python
  # tests/test_phrase.py
  def test_initial_example():
    assert False
  ```

  see `…/learn_python_01_package_008_tutorial/tests/test_phrase.py`  
  … commit `1914a82b42768559a97fe2e2437fe90cacf76f34`

  ``` bash
  …/learn_python_01_package_008_tutorial> pytest
  ================================ test session starts ================================
  platform linux -- Python 3.13.7, pytest-7.4.4, pluggy-1.6.0
  rootdir: /mnt/ntfs1/home.UserRus/Documents.Notes/learn_python_01_package_008_tutorial
  collected 1 item                                                                                                                                                                    

  tests/test_phrase.py .                                                                                                                                                        [100%]

  ================================= 1 passed in 0.02s =================================
  ```

### 8.2.1 A Useful Passing Test

- Having learned the basic mechanics of *GREEN* and *RED* tests,  
  … we’re now ready to write our first *useful* test.

- At first, wie implement the `Phrase` class in `src/palindrome_stonelouse/phrase.py`.

- Then we have to **install** our package in the *local environment*  
  … in order to *import* the package.

  ``` bash
  …/learn_python_01_package_008_tutorial> pip install -e .
  Obtaining file:///mnt/ntfs1/home.UserRus/Documents.Notes/learn_python_01_package_008_tutorial
    Installing build dependencies ... done
    Checking if build backend supports build_editable ... done
    Getting requirements to build editable ... done
    Installing backend dependencies ... done
    Preparing editable metadata (pyproject.toml) ... done
  Building wheels for collected packages: palindrome_stonelouse
    Building editable for palindrome_stonelouse (pyproject.toml) ... done
    Created wheel for palindrome_stonelouse: filename=palindrome_stonelouse-0.0.1-py3-none-any.whl size=2305 sha256=6910b6d50d32cf6b0042fdcc0f6161ad96976f03d163352d0e758f33ad095fd2
    Stored in directory: /tmp/pip-ephem-wheel-cache-p8cpv6cn/wheels/8b/dd/ed/32e3ff6469c196c2e6e37d06abfca70845b631f884cf524b8a
  Successfully built palindrome_stonelouse
  Installing collected packages: palindrome_stonelouse
  Successfully installed palindrome_stonelouse-0.0.1
  ```

  see `…/learn_python_01_package_008_tutorial/`  
  … commit `00e19ff623f3480675c1760f564f999653d5a7cc`

- After that, we can write and run our first test suite:

  ``` Python
  ## Our test suite for the Phrase class

  # Importing 'Phrase' in the test file
  from palindrome_stonelouse.phrase import Phrase

  def test_non_palindrome():
      assert not Phrase("apple").ispalindrome()

  def test_literal_palindrome():
      assert Phrase("racecar").ispalindrome()
  ```

  see `…/learn_python_01_package_008_tutorial/`  
  … commit `5ed21985292fb2b20919629eda038db900309151`

  ``` bash
  … /learn_python_01_package_008_tutorial> pytest
  ================================ test session starts ================================
  platform linux -- Python 3.13.7, pytest-7.4.4, pluggy-1.6.0
  rootdir: /mnt/ntfs1/home.UserRus/Documents.Notes/learn_python_01_package_008_tutorial
  collected 2 items                                                                                                                                                                  

  tests/test_phrase.py ..                                                        [100%]

  ================================= 2 passed in 0.03s =================================
  ```

### 8.2.2 Pending Tests - `skip()`

- Furthermore, we'll add a couple of **pending** tests,  
  … which are *placeholders*/ *reminders* for tests **we want to write later**.  

  The way to write a *pending* test is to use the ***`skip()`*** function.

  ``` Python
  ## Our test suite for the Phrase class

  # Importing 'Phrase' in the test file
  from unittest import skip
  from palindrome_stonelouse.phrase import Phrase

  def test_non_palindrome():
      assert not Phrase("apple").ispalindrome()

  def test_literal_palindrome():
      assert Phrase("racecar").ispalindrome()

  def test_mixed_case_palindrome():
    skip("Not implemented yet")

  def test_palindrome_with_punctuation():
      skip("Not implemented yet")
  ```

  ``` bash
  … /learn_python_01_package_008_tutorial> pytest
  ================================ test session starts ================================
  platform linux -- Python 3.13.7, pytest-7.4.4, pluggy-1.6.0
  rootdir: /mnt/ntfs1/home.UserRus/Documents.Notes/learn_python_01_package_008_tutorial
  collected 4 items                                                                                                                                                                  

  tests/test_phrase.py ....                                                      [100%]

  ================================= 4 passed in 0.03s =================================
  ```

  … the output looks different compared to the book?!

- In order to make 100% sure that the tests are testing what we think they’re testing,  
  … it’s a good practice to get to a **failing state** (*RED*)  
  … by **intentionally breaking** the tests.

  **Change the application code** to break each of the existing tests in turn,  
  … and then confirm that they are *GREEN* again **once the original code has been restored**.

  Apparently, you don't have to *re-install* or *reload* the package after the code change,  
  … changing the application code seems to be enough.

- Exercise 8.2.3

  see `…/learn_python_01_package_008_tutorial/`  
  … commit `700ccd11eaabdfc6ccf8d802cae73d7374cc49b1`
