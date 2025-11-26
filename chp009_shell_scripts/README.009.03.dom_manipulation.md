# 9. Shell Scripts

- TOC TODO

## 9.3 DOM Manipulation at the Commandline

- continued see [hartl](../README.md#hartl) p.245

- We want to implement a commandline script that  
  1. Takes an arbitrary URL argument at the command line
  1. Downloads the HTML
  1. Manipulates its content using the DOM
  1. Removes the references (anchor elements)
  1. Collects and prints the paragraph

- For HTML-processing, we use the [*"Beautiful Soap"*](https://pypi.org/project/beautifulsoup4/) package.  
  … which has a powerful HTML parser.

  see also  
  … [BeautifulSoup | home](https://www.crummy.com/software/BeautifulSoup/)  
  … [BeautifulSoup | doc](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

  ``` pwsh
  (.venv) PS D:\NoScan\home.rus\dev.ext.prj\learn-python-01> pip install beautifulsoup4 
  # …
  (.venv) PS D:\NoScan\home.rus\dev.ext.prj\learn-python-01> pip list
  Package           Version
  ----------------- -------
  beautifulsoup4    4.14.2  
  # …
  ```

  ``` Python
  >>> from bs4 import BeautifulSoup
  >>> html = '<p>lorem<sup class="reference">1</sup></p><p>ipsum</p>'
  >>> doc = BeautifulSoup(html)
  ```

- `bs4` provides a method [`find_all()`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all) which pulls out HTML tags.

  ``` Python
  >>> # …
  >>> doc.find_all("p")
  [<p>lorem<sup class="reference">1</sup></p>, <p>ipsum</p>]d
  ```

- This operation is so common, that it's the *default* when we pass an argument directly to the *document* object.

  ``` Python
  >>> # …
  >>> doc("p")
  [<p>lorem<sup class="reference">1</sup></p>, <p>ipsum</p>]
  >>> len(doc("p"))
  2
  >>> doc("p")[0].text
  'lorem1'
  ```

- the `text` property represents the text of a particular HTML element.

- Grabbing elements of a particular type which also have a particular class.

  ``` Python
  >>> doc("sup", class_="reference")
  [<sup class="reference">1</sup>]
  >>> len(doc("sup", class="reference"))
  1
  ```
