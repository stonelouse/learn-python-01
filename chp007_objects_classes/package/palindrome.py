class Phrase:
  """A class to represent phrases."""

  def __init__(self, content):
    self.content = content

# The next line arranges
# … to execute the subsequent code
# … if the file is run at the command line
# … but not when the class is loaded into other files
# … see https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
  # creating a Phrase instance
  phrase = Phrase("Madam, I'm Adam")
  print(phrase.content)

  phrase.content = "Able was I, ere I saw Elba"
  print(phrase.content)
