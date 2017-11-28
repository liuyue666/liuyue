Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> L=[1,2,3]
>>> I=iter(L)
>>> for i in I:
	print(i, end='-')
	
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> next(I)
1
>>> I=iter(L)
>>> J=I
>>> next(I)
1
>>> next(J)
2
>>> next(I)
3
>>> next(J)

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    next(J)
StopIteration
>>> import copy
>>> I=iter(L)
>>> J=copy.deepcopy(I)

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    J=copy.deepcopy(I)
  File "C:\Python27\lib\copy.py", line 182, in deepcopy
    rv = reductor(2)
TypeError: can't pickle listiterator objects
>>> next(I)
1
>>> next(I)
2
>>> next(J)

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    next(J)
StopIteration
>>> 
