def reverse(string):
    """Reverse a string."""
    return "".join(reversed(string))


def is_palindrome(string):
    """Return True for a palindrome, False otherwise."""
    string_prepared = string.lower()
    return string_prepared == reverse(string_prepared)
