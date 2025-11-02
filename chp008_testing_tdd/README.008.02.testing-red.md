# 8. Testing and Test-Driven Development

## 8.3 Red

- continued see [hartl](../README.md#hartl) p.209

- Now, we want to be able to detect more complex palindromes like  
  > “Madam, I’m Adam.” and “A man, a plan, a canal Panama!”.
  
- Unlike the previous strings we’ve encountered, these phrases — which contain both *spaces* and *punctuation* — *aren’t strictly palindromes in a literal sense*,
even if we ignore *capitalization*.

- Instead of testing the strings as they are, *we have to figure out a way*  
  … to *select only the letters*, and  
  … then see if the resulting letters are the same forward and backward.

- The *code to do this is fairly tricky*, **but the tests for it are simple**.  
  … This is one of the situations where **test-driven development** particularly *shines*  
  … see Box 8.1: When to test on p.209:

  - Automatic Tests protect against *regressions*
  - Automatic Tests allow code to be *refactored*
  - Tests act as a *client* for the application code

  … We can write our *simple tests*, thereby getting to *RED*, and then *write the application code* any way we want to get to *GREEN*.
  
- At that point, with the tests protecting us against **undiscovered errors**, we can change the application code with confidence.

### Guidlines - What should I write first

- When a *test* is especially **short or simple** compared to the *application code* it tests,  
  … lean toward writing the **test first**.
- When the desired **behavior isn’t yet crystal clear**,  
  … lean toward writing the **application code first**,  
  … then write a *test* to codify the result.
- Whenever a **bug is found**,  
  … **write a test** to reproduce it and protect against regressions,  
  … then write the *application code to fix it*.
- Write **tests before refactoring code**,  
  … *focusing on testing error-prone code* that’s especially likely to break.

### RED Test for palindrome with punctuation

- see `…/learn_python_01_package_008_tutorial/tests/test_phrase.py`  
  … commit `057c83a2c2e4a497ba556d12120d849ee58be3f5`

  ``` Python
  # test_phrase.py
  # …
  def test_palindrome_with_punctuation():
      assert Phrase("Madam, I'm Adam.").ispalindrome()
  # …
  ```

### Add a test for a new yet unimplemented method `.letters()`

- Our strategy will be to write a `.letters()` method  
  … that returns only the *letters* in the `content` string.
  
- Having made this *specification*, we implement a *simple test* for `.letters()`  
  
  ``` Python
  # test_phrase.py
  # …
  def test_letters():
      assert Phrase("Madam, I'm Adam.").letters() == "MadamImAdam"
  # …
  ```

  … and then we implement a **stub** - a method that doesn't work, but at least exists.

  ``` Python
  # phrase.py
  # …
  def letters(self):
    """Return only the letters in the content."""
    pass
  # …
  ```  

- The new test for `.letters()` is also *RED*, as expected.

- With these two *RED* tests **capturing the desired behavior**,  
  … we are now ready to move on the *application code* and try getting it to *GREEN*.
