# 7. Objects and Classes

- Todo

## 7.3 Inheritance

- continued see [hartl](../README.md#hartl) p.179

### Investigating *class hierarchy* - `__class__`, `__mro__`

- When learning about Python classes, it’s useful to investigate the *class hierarchy* using  
  - the **`__class__`** and  
  - the **`__mro__`**  
  
  *attributes*.

  The latter stands for *method resolution order*.

  Let's look at an example of what this means in the case of a familiar type of *object*, a *string*:

  ``` Python
  >>> s = "foobar"
  >>> type(s)
  <class 'str'>
  >>> s.__class__
  <class 'str'>
  >>> s.__class__.__mro__
  (<class 'str'>, <class 'object'>)
  >>> 
  ```

- What this tells us is that a *string* is of **class** `str`,  
  … which in turn is of type *object*.  
  
  The latter is known as a **superclass**  
  … because it is usually thought of as being “above” the `str` class.

- `object` is the *superclass* of every Python *object*.

- The `__class_` attribute is inherited from `object`.

  ``` Python
  >>> obj = object()
  >>> type(obj)
  <class 'object'>
  AttributeError: 'object' object has no attribute '__mro__'
  >>> obj.__class__
  <class 'object'>
  >>> object().__class__
  <class 'object'>
  >>> type(obj.__class__)
  <class 'type'>  
  ```

### *Composition* vs. *Inheritance*

- Let’s return now to the `Phrase` *class*
  
- As presently defined, `Phrase` **has a** `content` *attribute*,  
  … which in the terminology of *object-oriented programming* is known as a **has-a relationship**.  
  … Such a design is known as **composition**,  
  … where a `Phrase` is **composed** of a `content` *attribute* (possibly among other things).  

  ![Composition - has a](./image.007.03.01.composition.png)

- Another way of looking at the situation is to say that a `Phrase` **is a** `string`,  
  … which is known as an **is-a relationship**.  
  … In this case, we could arrange for the `Phrase` class to **inherit** from Python’s native `string` class.

  ![Inheritance - is a](./image.007.03.02.inheritance.png)

- Exercise 7.3.1

  ``` Python
  >>> [].__class__
  <class 'list'>
  >>> [].__class__.__mro__
  (<class 'list'>, <class 'object'>)
  >>> {}.__class__
  <class 'dict'>
  >>> {}.__class__.__mro__
  (<class 'dict'>, <class 'object'>)
  ```

## 7.4 Derived Class

- continued see [hartl](../README.md#hartl) p.179

- Now we want to derive a new class `TranslatedPhrase` from the `Phrase` class.  
  … The purpose of this so-called **derived** class (or **subclass**) is  
  … to **reuse** as much of `Phrase` as possible  
  …  while giving us the **flexibility** to, say, test if a `translation` is a palindrome.

- We *derive* from `Phrase` by passing the *super class*' name as argument.

- Inside the `__init__` method of our *derived* class, we call Python's *special function* **`super()`**,  
  … passing the argument of the `content` parameter.

- Because `TranslatedPhrase` *inherits* from `Phrase`, an *instance* of `TranslatedPhrase` **automatically has all the methods and attributes** of a `Phrase` instance.

  ``` Python
  class Phrase:
    """A class to represent phrases."""

    def __init__(self, content):
      self.content = content

    def ispalindrome(self):
      """Return True for a palindrome, False otherwise."""
      return self.processed_content() == reverse(self.processed_content())

    def processed_content(self):
      """Process content for palindrome testing."""
      return self.content.lower()

    def __iter__(self):
      self.phrase_iterator = iter(self.content)
      return self
    
    def __next__(self):
      return next(self.phrase_iterator)

  class TranslatedPhrase(Phrase):
    """A class to represent phrases with translation."""

    def __init__(self, content, translation):
      # setting `content`
      super().__init__(content)
      self.translation = translation

  def reverse(string):
    """Reverse a string."""
    return "".join(reversed(string))
  ```

  ``` Python
  # REPL
  PS D:\NoScan\home.rus\dev.ext.prj\learn-python-01\chp007_objects_classes\package> ..\..\venv\Scripts\Activate.ps1
  (venv) PS D:\NoScan\home.rus\dev.ext.prj\learn-python-01\chp007_objects_classes\package> python
  Python 3.13.6 (tags/v3.13.6:4e66535, Aug  6 2025, 14:36:00) [MSC v.1944 64 bit (AMD64)] on win32
  Type "help", "copyright", "credits" or "license" for more information.
  Ctrl click to launch VS Code Native REPL
  >>> import importlib
  >>> import palindrome as palindrome
  >>> tphrase = palindrome.TranslatedPhrase("Madam", "Dame")  
  >>> tphrase = palindrome.TranslatedPhrase("Madam", "Frau") 
  >>> tphrase.content
  'Madam'
  >>> tphrase.translation
  'Frau'
  >>> tphrase.ispalindrome()
  True
  ```
