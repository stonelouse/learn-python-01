# 4. Other Native Objects

- TODO TOC

## 4.2 Time and Datetime

- continued see [hartl](../README.md#hartl) p.97

### `time` Module

- see <https://docs.python.org/3/library/time.html#time.ctime>
  > … provides various *time-related functions*.  
  > … Although this module is always available, **not all functions are available on all platforms**. Most of the functions defined in this module call *platform C library functions* with the same name.

- [`time.time()`](https://docs.python.org/3/library/time.html#time.time) returns the number of seconds since the *epoch*, defined as *January 1, 1970*.  
  … [`time.ctime()`](https://docs.python.org/3/library/time.html#time.ctime) get a conveniently formatted string

  ``` Python
  >>> import time
  >>> time.time()
  1756699417.4412646
  >>>
  >>> time.ctime()
  'Mon Sep  1 06:04:21 2025'
  ```

### `datetime` Module

- see <https://docs.python.org/3/library/datetime.html#module-datetime>
  > … supplies classes for manipulating dates and times.

- This module provides a class with the same name [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime) which provides various useful methods:

  ``` Python
  >>> import datetime
  >>> now = datetime.datetime.now()
  >>> now
  datetime.datetime(2025, 9, 1, 6, 14, 39, 697752)
  >>> now.year
  2025
  >>> now.month
  9   
  >>> now.day
  1   
  >>> now.hour
  6   
  >>> now.minute
  14  
  >>> now.second
  39  
  >>> now.microsecond
  697752
  ```

- Because many useful methods are defined on the separate `datetime` *object* **within**
the `datetime` *module*, it’s often more convenient to use `from` to *import* just that one
object.

- see <https://docs.python.org/3/library/datetime.html#datetime.datetime.utcnow>:  
  > Because naive `datetime` objects are treated by many `datetime` *methods* as **local times**, it is preferred to use *aware datetimes* to **represent times in UTC**. As such, the **recommended way** to create an object representing the **current time in UTC** is by calling `datetime.now(timezone.utc)`.

  ``` Python
  >>> from datetime import datetime, timezone
  >>> now_local = datetime.now()
  >>> now_local
  datetime.datetime(2025, 9, 1, 6, 23, 39, 616926)
  >>> now_utc = datetime.now(timezone.utc)
  >>> now_utc
  datetime.datetime(2025, 9, 1, 4, 23, 59, 102631, tzinfo=datetime.timezone.utc)
  ```

  - For most practical purposes, *Coordinated Universal Time (UTC)* is the same as *Greenwich Mean Time*.

- Creating `datetime` *objects* with the `datetime` *function*  
  … using a **keyword argument** `tzinfo`

  ``` Python
  >>> moon_landing_utc = datetime(1969, 7, 20, 20, 17, 40, tzinfo=timezone.utc)
  >>> moon_landing_utc
  datetime.datetime(1969, 7, 20, 20, 17, 40, tzinfo=datetime.timezone.utc)
  >>> print (moon_landing_utc)
  1969-07-20 20:17:40+00:00
  ```
