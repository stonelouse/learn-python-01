# user@ideapad:~/home_rus/learn-python-01/chp005_functions_iterators$ python ./p005.01.greet.py

from package.p005_02_is_palindrome import is_palindrome

string = "kayak"
print(f"'{string}' is a palindrome: {is_palindrome(string)}")

string = "foobar"
print(f"'{string}' is a palindrome: {is_palindrome(string)}")

string = "racecar"
print(f"'{string}' is a palindrome: {is_palindrome(string)}")

string = "R( acecar"
print(f"'{string}' is a palindrome: {is_palindrome(string)}")

string = ""
print(f"'{string}' is a palindrome: {is_palindrome(string)}")
