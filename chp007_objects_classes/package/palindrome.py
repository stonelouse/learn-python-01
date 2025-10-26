class Phrase:
  """A class to represent phrases."""

  def __init__(self, content):
    self.content = content

  def ispalindrome(self):
    """Return True for a palindrome, False otherwise."""
    return self._processed_content() == reverse(self._processed_content())

  def _processed_content(self):
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

  def _processed_content(self):
    """Override superclass method to use translation."""
    return self.translation.lower()

def reverse(string):
  """Reverse a string."""
  return "".join(reversed(string))
