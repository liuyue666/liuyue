Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Iterable:
	def __iter__(self):
		return Iterator()

	
>>> class Iterator:
	def __init__(self):
		self.start=-1
	def __next__(self):
		self.start +=2
		if self.start >10:
		    raise StopIteration
		return self.start

	
>>> I = Iterable()
>>> for i in I:
	print(i)

	

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    for i in I:
TypeError: instance has no next() method
>>> I = Iterable()
>>> for count, i in zip(range(5),I):
	print(i)
	
