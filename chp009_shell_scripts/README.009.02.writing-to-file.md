# 9. Shell Scripts

- [9. Shell Scripts](#9-shell-scripts)
  - [9.2 Writing to a file](#92-writing-to-a-file)

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
