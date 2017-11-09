Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import re
>>> print(re.match('www','www.runoob.com').span())
(0, 3)
>>> print(re.match('com','www.runoob.com'))
None
>>> 
