# user@ideapad:~/home_rus/learn-python-01/chp005_functions_iterators$ python3 ./p005.01.greet.py 

from datetime import datetime

from package.p005_01_day import dayname


print(f"Today is {dayname(datetime.now())}")
