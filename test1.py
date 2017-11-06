Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Employee:
   '所有员工的基类'
   empCount = 0
 
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount
 
   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

      
>>> 
>>> 
>>> e = Employee ('刘月','10')
>>> e.displayCount()
Total Employee 1
>>> e.displayEmployee()
Name :  刘月 , Salary:  10
>>> 
>>> e = Employee('刘月2','20')
>>> e.displayCount()
Total Employee 2
>>> 
>>> e.displayEmployee()
Name :  刘月2 , Salary:  20
>>> 
