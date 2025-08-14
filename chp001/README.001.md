# 1. Introduction - "Hello World"

- [1. Introduction - "Hello World"](#1-introduction---hello-world)
  - [1.2. Python in a REPL](#12-python-in-a-repl)
  - [1.3 Python in a File](#13-python-in-a-file)
    - [Self contained virtual environments](#self-contained-virtual-environments)
    - [`venv` and `pip` package](#venv-and-pip-package)
    - [Creating a virtual environment](#creating-a-virtual-environment)
    - [Implement and run first Python program](#implement-and-run-first-python-program)
  - [1.4 Python in a Shell Script](#14-python-in-a-shell-script)
  - [1.5 Python in a Web Server](#15-python-in-a-web-server)
    - [Flask](#flask)
    - [pip command](#pip-command)

## 1.2. Python in a REPL

- see [hartl](../README.md#hartl) p.11
- REPL: _Read/Eval/Print Loop_

- Python REPL is also known as **Python interpreter** or **Python shell**

- Starting the REPL

  ``` pwsh
  PS D:\home.UserRus\Documents.Notes\__learn-python-01> python
  Python 3.13.6 (tags/v3.13.6:4e66535, Aug  6 2025, 14:36:00) [MSC v.1944 64 bit (AMD64)] on win32
  Type "help", "copyright", "credits" or "license" for more information.
  >>> print("hello world");
  hello world
  >>>
  ```

- "The Zen of Python"

  ``` pwsh
  PS D:\NoScan\home.rus\dev.ext.prj\learn-python-01> python
  Python 3.13.6 (tags/v3.13.6:4e66535, Aug  6 2025, 14:36:00) [MSC v.1944 64 bit (AMD64)] on win32
  Type "help", "copyright", "credits" or "license" for more information.
  >>> import this
  The Zen of Python, by Tim Peters

  Beautiful is better than ugly.
  Explicit is better than implicit.
  Simple is better than complex.
  Complex is better than complicated.
  Flat is better than nested.
  Sparse is better than dense.
  Readability counts.
  Special cases aren't special enough to break the rules.
  Although practicality beats purity.
  Errors should never pass silently.
  Unless explicitly silenced.
  In the face of ambiguity, refuse the temptation to guess.
  There should be one-- and preferably only one --obvious way to do it.
  Although that way may not be obvious at first unless you're Dutch.
  Now is better than never.
  Although never is often better than *right* now.
  If the implementation is hard to explain, it's a bad idea.
  If the implementation is easy to explain, it may be a good idea.
  Namespaces are one honking great idea -- let's do more of those!
  >>> 
  ```

- Keyword argument `end`

  ``` pwsh
  >>> print("Hello world", end="")
  >>> o world
  >>> print("Hello world", end="<")
  >>> o world<
  >>> print("Hello world", end="\n")
  Hello world
  >>>
  ```

## 1.3 Python in a File

- see [hartl](../README.md#hartl) p.13

### Self contained virtual environments

- *Self contained virtual environments_ allows us  
  … to use the exact version of Python we want  
  … without affecting the rest of the system.

### `venv` and `pip` package

- We use these two packages to install additional packages.
- All of the specifics of the setup are contained in a single directory.
- Alternatively, we can use the `conda` package for this.

### Creating a virtual environment

- We use the option `-m`. `-m` stands for `module`,  
  … pass `venv` as _name of the virtual environment module*  
  … and a name `venv` (of our choice)  
  … to create a virtual environment

- Python's [venv](https://docs.python.org/3/library/venv.html) in action

  ``` pwsh
  PS D:\NoScan\home.rus\dev.ext.prj\learn-python-01> python -m venv venv

  PS D:\NoScan\home.rus\dev.ext.prj\learn-python-01\venv> ls

      Directory: D:\NoScan\home.rus\dev.ext.prj\learn-python-01\venv

  Mode                 LastWriteTime         Length Name
  ----                 -------------         ------ ----
  d----           8/13/2025 07:12 AM                Include
  d----           8/13/2025 07:12 AM                Lib
  d----           8/13/2025 07:12 AM                Scripts
  -a---           8/13/2025 07:12 AM             71 .gitignore
  -a---           8/13/2025 07:12 AM            210 pyvenv.cfg

  PS D:\NoScan\home.rus\dev.ext.prj\learn-python-01> $env:VIRTUAL_ENV
  PS D:\NoScan\home.rus\dev.ext.prj\learn-python-01> .\venv\Scripts\Activate.ps1 
  (venv) PS D:\NoScan\home.rus\dev.ext.prj\learn-python-01> $env:VIRTUAL_ENV
  D:\NoScan\home.rus\dev.ext.prj\learn-python-01\venv
  (venv) PS D:\NoScan\home.rus\dev.ext.prj\learn-python-01> deactivate
  PS D:\NoScan\home.rus\dev.ext.prj\learn-python-01> $env:VIRTUAL_ENV
  PS D:\NoScan\home.rus\dev.ext.prj\learn-python-01>
  ```

### Implement and run first Python program

- Implement `p01-hello-world.py` and run it

  ``` pwsh
  PS D:\home.UserRus\Documents.Notes\__learn-python-01> python -m venv venv        
  PS D:\home.UserRus\Documents.Notes\__learn-python-01> New-Item -Type file .\chp001\p01-hello-world.py

      Directory: D:\home.UserRus\Documents.Notes\__learn-python-01\chp001

  Mode                 LastWriteTime         Length Name
  ----                 -------------         ------ ----
  -a---          14.08.2025    19:27              0 p01-hello-world.py

  PS D:\home.UserRus\Documents.Notes\__learn-python-01> .\venv\Scripts\Activate.ps1
  (venv) PS D:\home.UserRus\Documents.Notes\__learn-python-01> python .\chp001\p01-hello-world.py
  Hello, World!
  Hello, World! how is it going?
  (venv) PS D:\home.UserRus\Documents.Notes\__learn-python-01> 
  ```

## 1.4 Python in a Shell Script

- see [hartl](../README.md#hartl) p.16

- We implemented `p02-hello-world-script`. For this, we opened a _git bash_

  ``` bash
  (venv)
  chris@ARLT MINGW64 /d/home.UserRus/Documents.Notes/__learn-python-01 (main)
  $ ls -la ./chp001/p02-hello-world-script 
  -rwxr-xr-x 1 chris 197609 64 Aug 14 18:12 ./chp001/p02-hello-world-script*  
  (venv)
  chris@ARLT MINGW64 /d/home.UserRus/Documents.Notes/__learn-python-01 (main)
  $ ./chp001/p02-hello-world-script 
  Hello, World! from script
  ```

## 1.5 Python in a Web Server

- see [hartl](../README.md#hartl) p.18

### Flask

- [Flask](https://flask.palletsprojects.com/) micro-framework

### pip command

- `pip` – "_pip installs packages_"  
  … part of `venv`

``` pwsh
# Upgrade pip
(venv) PS D:\home.UserRus\Documents.Notes\__learn-python-01> pip install --upgrade pip
Requirement already satisfied: pip in d:\home.userrus\documents.notes\__learn-python-01\venv\lib\site-packages (25.2)

# Install Flask
(venv) PS D:\home.UserRus\Documents.Notes\__learn-python-01> pip install Flask

# Create app file; … implementation follows
(venv) PS D:\home.UserRus\Documents.Notes\__learn-python-01> New-Item -Type file ./chp001/p03-hello-app.py     

    Directory: D:\home.UserRus\Documents.Notes\__learn-python-01\chp001

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---          14.08.2025    18:32              0 p03-hello-app.py

# Run app
(venv) PS D:\home.UserRus\Documents.Notes\__learn-python-01> flask --app .\chp001\p03-hello-app.py --debug run
 * Serving Flask app '.\chp001\p03-hello-app.py'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 894-431-672
127.0.0.1 - - [14/Aug/2025 18:34:58] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [14/Aug/2025 18:34:58] "GET /favicon.ico HTTP/1.1" 404 -
```
