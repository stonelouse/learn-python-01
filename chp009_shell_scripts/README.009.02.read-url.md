# 9. Shell Scripts

- [9. Shell Scripts](#9-shell-scripts)
  - [9.2 Reading from URLs](#92-reading-from-urls)

## 9.2 Reading from URLs

- continued see [hartl](../README.md#hartl) p.241

- For reading content from URLs we use the [`requests` package](https://pypi.org/project/requests/), which we can install using _pip_

  ``` bash
  …/__learn-python-01> pip install requests
  …
  …/__learn-python-01> pip list
  …
  requests              2.32.5
  ```

  ``` Python
  >>> import requests
  >>> url = "https://cdn.learnenough.com/phrases.txt"
  >>> response = requests.get(url)
  >>> response.text.splitlines()
  ['A butt tuba', 'A bad penny always turns up.', 'A fool and his money are soon parted.', 'A man, a plan, …]
  >>>
  ```

- see `chp009_shell_scripts/palindrome_url_read_file_write.py` commit `c0d6f806`

  The result is pretty the same as before when we read `phrases` from a file.  
  … But we have an _encoding_ issue:  

  ``` plain text
  …
  A man, a plan, a canalâPanama!
  …
  ```

- see `chp009_shell_scripts/palindrome_url_read_file_write.py` commit `c2f696a5` for the version that fixed this issue:

  ``` plain text
  …
  A man, a plan, a canal—Panama!
  …
  ```
