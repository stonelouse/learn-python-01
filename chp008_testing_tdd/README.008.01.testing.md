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
