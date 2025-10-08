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
  commit `Todo`

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
