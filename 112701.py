Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> L = [1,2,3]
>>> [x**2 for x in L]
[1, 4, 9]
>>> next(L)

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    next(L)
TypeError: list object is not an iterator
>>> I=iter(L)
>>> next(I)
1
>>> next(I)
2
>>> next(I)
3
>>> next(I)

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    next(I)
StopIteration
>>> 
