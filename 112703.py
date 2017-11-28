Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from collections import Iterator, Iterable
>>> help(Iterator)
Help on class Iterator in module _abcoll:

class Iterator(Iterable)
 |  Method resolution order:
 |      Iterator
 |      Iterable
 |      __builtin__.object
 |  
 |  Methods defined here:
 |  
 |  __iter__(self)
 |  
 |  next(self)
 |      Return the next item from the iterator. When exhausted, raise StopIteration
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __subclasshook__(cls, C) from abc.ABCMeta
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __abstractmethods__ = frozenset(['next'])
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Iterable:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from Iterable:
 |  
 |  __metaclass__ = <class 'abc.ABCMeta'>
 |      Metaclass for defining Abstract Base Classes (ABCs).
 |      
 |      Use this metaclass to create an ABC.  An ABC can be subclassed
 |      directly, and then acts as a mix-in class.  You can also register
 |      unrelated concrete classes (even built-in classes) and unrelated
 |      ABCs as 'virtual subclasses' -- these and their descendants will
 |      be considered subclasses of the registering ABC by the built-in
 |      issubclass() function, but the registering ABC won't show up in
 |      their MRO (Method Resolution Order) nor will method
 |      implementations defined by the registering ABC be callable (not
 |      even via super()).

>>> 
