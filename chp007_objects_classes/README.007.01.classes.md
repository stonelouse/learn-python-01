# 7. Objects and Classes

- Todo

## 7.1 Defining Classes

- continued see [hartl](../README.md#hartl) p.1169

- **Classes** are defined by using the [**`class`**](https://docs.python.org/3/tutorial/classes.html#class-definition-syntax) *keyword*.

- Use the special [**`__init__`**](https://docs.python.org/3/reference/datamodel.html#object.__init__) method (***initializer function***) to specify how to initialize a class.

- `Phrase` class

  see `chp007_objects_classes\package\palindrome.py`  
  commit `a696db81d5dc16d77b523b40fbf21c38b2293488`

  ``` Python
  class Phrase:
    """A class to represent phrases."""

  # The next line arranges
  # … to execute the subsequent code
  # … if the file is run at the command line
  # … but not when the class is loaded into other files
  # … see https://docs.python.org/3/library/__main__.html
  if __name__ == "__main__":
    # creating a Phrase instance
    phrase = Phrase()
    print(phrase)
  ```

  Running the code above:

  ``` Python
  (venv) PS D:\NoScan\home.rus\dev.ext.prj\learn-python-01> python .\chp007_objects_classes\package\palindrome.py
  <__main__.Phrase object at 0x00000207BF0D6A50>
  ```

- This shows Python’s *abstract internal representation* of a *bare instance* of the `Phrase` class.  
  … We also see where the value `__main__` comes from in if `__name__ == "__main__"`,  
  … it’s the "**top-level code environment**", which is the environment (containing classes, functions, variables, etc.) in which Python *shell scripts* are **executed**.

- Unlike *variables* and *methods*, Python *class names* use **CamelCase** instead of *snake_case*.

### Defining the `__init__` initializer function and *data attributes*

- We'll define `Phrase's` **initializer function**,  
  … that takes an *argument* *`content`* and  
  … set a **data attribute** called *`content`*.

- `Phrase` class

  see `chp007_objects_classes\package\palindrome.py`  
  commit `16e8620f0a93153bba12df0a527744d3fcd82c48`

  ``` Python
  class Phrase:
    """A class to represent phrases."""

    def __init__(self, content):
      self.content = content

  if __name__ == "__main__":
    # creating a Phrase instance
    phrase = Phrase("Madam, I'm Adam")
    print(phrase.content)
  ```

  Running the code above:

  ``` Python
  PS …\learn-python-01> python .\chp007_objects_classes\package\palindrome.py
  Madam, I'm Adam
  ```

### Assigning to an *object attribute* - *dot notation*

- We can also now assign directly to the object's attribute `content`  
  … using the **dot notation**:

  see `chp007_objects_classes\package\palindrome.py`  
  commit `89f0eb4070d24fe42f339804f1f4a7d508ad28e8`

  ``` Python
  # …
  if __name__ == "__main__":
    # creating a Phrase instance
    phrase = Phrase("Madam, I'm Adam")
    print(phrase.content)

    phrase.content = "Able was I, ere I saw Elba"
    print(phrase.content)
  ```

  ``` bash
  …/__learn-python-01/chp007_objects_classes> python3 ./package/palindrome.py 
  Madam, I'm Adam
  Able was I, ere I saw Elba
  ```

### Adding the functions `reverse()` and `ispalindrome()`

- Now we remove the `if __name__ == "__main__"` section and replace it with the function definitions of `reverse()` and `ispalindrome()` from `../chp005_functions_iterators/package/p005_02_is_palindrome.py`:

  see `chp007_objects_classes\package\palindrome.py`  
  commit `44c9dd62cc7a5ca2b5f52fbd2ade9bd991f9dc03`

  ``` Python
  class Phrase:
    """A class to represent phrases."""

    def __init__(self, content):
      self.content = content

  def reverse(string):
    """Reverse a string."""
    return "".join(reversed(string))

  def ispalindrome(string):
    """Return True for a palindrome, False otherwise."""
    processed_content = string.lower()
    return processed_content == reverse(processed_content)
  ```

- Then we test our changes in the REPL

  ``` bash
  …/__learn-python-01/chp007_objects_classes/package> python3
  Python 3.13.7 (main, Sep 28 2025, 13:03:11) [GCC 7.5.0] on linux
  Type "help", "copyright", "credits" or "license" for more information.
  Ctrl click to launch VS Code Native REPL
  >>> import palindrome
  >>> phrase = palindrome.Phrase("Racecar")
  >>> palindrome.ispalindrome(phrase.content)
  True
  ```
