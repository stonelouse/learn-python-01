# 9. Shell Scripts

- [9. Shell Scripts](#9-shell-scripts)
  - [9.1 Reading from Files](#91-reading-from-files)
  - [9.2 Writing to a file](#92-writing-to-a-file)

## 9.1 Reading from Files

- continued see [hartl](../README.md#hartl) p.231

- Python handles file operations natively.  
  - [`open()`](https://docs.python.org/3/library/functions.html#open)  
    … Open file and return a corresponding [`file`](https://docs.python.org/3/glossary.html#term-file-object) object.
  - [`read()`](https://docs.python.org/3/library/io.html#io.TextIOBase.read)  
    … Read the file’s contents as a string (or up to size bytes when given);  
    … returns an empty string at EOF.
  - [`close()`](https://docs.python.org/3/library/io.html#io.IOBase.close)  
    … Flush and close this stream.

  ``` Python
  (venv) PS D:\NoScan\home.rus\dev.ext.prj\learn-python-01\chp009_shell_scripts> python
  >>> file = open("my_phrases.txt")
  >>> text = file.read() 
  >>> text
  "Madam, I'm Adam.\nRacecar\nSchiff\n"
  >>> print(text)
  Madam, I'm Adam.
  Racecar
  Schiff

  >>> file.close()
  >>> 
  ```

- Using the [`splitlines()`](../chp003.lists/README.003.01.md#splitlines-method) method,  
  … we can create a *list of lines*.

  ``` Python
  # …
  >>> text.splitlines()
  ["Madam, I'm Adam.", 'Racecar', 'Schiff']
  >>> text.splitlines()[1]
  'Racecar'
  >>>   
  ```

- Opening a file as shown above, **ISN’T fully Pythonic**.
  … The reason is that **we have to remember to close the file** every time we open one,  
  … which can cause **unpredictable behavior if we forget**.  
  
- We can avoid such issues by using the special **`with` keyword**,  
  … together with **as** and the **desired filename**:

  ``` Python
  >>> with open("my_phrases.txt") as file: # Pythonic!
  ...   text = file.read();
  ...   
  >>> len(text)
  32
  ```

  This code arranges to **close the file automatically**  
  … at the end of the `with` statement.

- Now we use the locally installed *package* `palindrome_stonelouse`

  ``` Python
  from palindrome_stonelouse.phrase import Phrase

  with open("phrases.txt") as file:
      text = file.read()
      for line in text.splitlines():  # Arguably not Pythonic!
          if Phrase(line).ispalindrome():
              print(f"palindrome detected: {line}")
  ```

  see `./palindrome_file.py` commit `4c2104505bfb0ccdf49b56a73c9e53d5b9b73eca`.
  4c2104505bfb0ccdf49b56a73c9e53d5b9b73eca

  ``` pwsh
  PS D:\NoScan\home.rus\dev.ext.prj\learn-python-01\chp009_shell_scripts> pip list
  Package               Version Editable project location
  --------------------- ------- -------------------------------------------------------------------
  palindrome_stonelouse 0.0.1   D:\NoScan\home.rus\dev.ext.prj\learn_python_01_package_008_tutorial
  pip                   25.3
  PS D:\NoScan\home.rus\dev.ext.prj\learn-python-01\chp009_shell_scripts> python .\palindrome_file.py
  palindrome detected: A butt tuba
  palindrome detected: A man, a plan, a canal—Panama!
  …
  ```

  ``` bash
  user@linux:/mnt/ntfs1/home.UserRus/Documents.Notes/__learn-python-01> pip list
  Package               Version Editable project location
  --------------------- ------- ----------------------------------------------------------------------------
  …
  palindrome_stonelouse 0.0.1   /mnt/ntfs1/home.UserRus/Documents.Notes/learn_python_01_package_008_tutorial
  …
  ```

- We have to consider that the package `palindrome_stonelouse` seems not to be installed or available, if we run the script in a *venv*

  ``` pwsh
  (.venv) PS D:\NoScan\home.rus\dev.ext.prj\learn-python-01\chp009_shell_scripts> pip list
  Package Version
  ------- -------
  pip     25.3
  ```

  ``` bash
  user@linux:/mnt/ntfs1/home.UserRus/Documents.Notes/__learn-python-01/chp009_shell_scripts> ./palindrome_file.py 
  palindrome detected: A butt tuba
  palindrome detected: A man, a plan, a canal—Panama!
  …
  ```

- Using [`file.readline()`](https://docs.python.org/3/library/io.html#io.IOBase.readline) results in a more pythonic approach:

  ``` Python
  from palindrome_stonelouse.phrase import Phrase

  with open("phrases.txt") as file:
    for line in file.readlines():  # Pythonic!
        if Phrase(line).ispalindrome():
            print(f"palindrome detected: {line}")  
  ```

  see `./palindrome_file.py` commit id `1d408034105cbf4d21c016901c6c8ff05409d1c6`.

  ``` bash
  user@linux:/mnt/ntfs1/home.UserRus/Documents.Notes/__learn-python-01/chp009_shell_scripts> ./palindrome_file.py 
  palindrome detected: A butt tuba

  palindrome detected: A man, a plan, a canal—Panama!
  …
  ```

- Now, there are extra newlines between the palindorme lines,  
  … which is dure to each element includes the newline.  
  … In order to replicate the previous output, we use [`.strip()`](https://docs.python.org/3/library/stdtypes.html#str.strip)  
  … **to remove *leading* and *trailing* whitespace**.  
  … but it comes at the cost of an additional call to `.strip()`,  
  … she `.splitlines()` version is *defensible as well*.

  ``` Python
  # …
              print(f"palindrome detected: {line.strip()}")  
  ```

  see `./palindrome_file.py` commit id `7b273cfc9114ddabea0e23cdd6fe43646faba401`.

## 9.2 Writing to a file

- continued see [hartl](../README.md#hartl) p.237

- With [write()](https://docs.python.org/3/library/io.html#io.TextIOBase.write) we can write into a file.  
  … see `chp009_shell_scripts/palindrome_file_write.py` commit `50093cdf0252ad803946619865af50a7b90d8bef`

- One *common pattern* in Python *shell scripts*  
  … is to put the *main steps* in a **separate function** (often called **`main()`**)  
  … and then call the function only when the **file itself is called as a shell script**.  
  
  See this video (<https://www.youtube.com/watch?v=g_wlZ9IhbTs>) for more:  
  … `if __name__ == '__main__':` signals that the file should be executed,  
  … otherwise you can assume that it is a library or should be *imported*.  
  … Further more, declare a `main` fundtion and call it to avoid declaring  global variables by accident.

  … see `chp009_shell_scripts/palindrome_file_write.py` commit `850c54374836701245d427ec98852163b798f3d9`.
