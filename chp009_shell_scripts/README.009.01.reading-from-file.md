# 9. Shell Scripts

- TOC TODO

## 9.1 Reading from Files

- continued see [hartl](../README.md#hartl) p.231

- Python handles file operations natively.  
  - [`open()`](TODO) … TODO
  - [`read()`](TODO) … TODO
  - [`close()`](TODO) … TODO

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

