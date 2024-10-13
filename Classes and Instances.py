Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #object oriented programming
>>> class Employee:
...     def __init__(self, first, last, pay):
...         self.first = first
...         self.last = last
...         self.pay = pay
...     def fullname(self):
...         return '{}{}'.format(self.first, self.last)
... 
...     
>>> emp_1 = Employee ('Jonathan', 'Wainaina', 20000)
>>> emp_2 = Employee ('June', 'Njeri', 20000)
>>> 
>>> print(emp_1.fullname)
<bound method Employee.fullname of <__main__.Employee object at 0x000002841D31C800>>
>>> #note that fullname without parentheses returns the position instead of the actual fullname
>>> print(emp_1.fullname())
JonathanWainaina
>>> print(Employee.fullname(emp_1))
JonathanWainaina
>>> #using the emp_.fullname gives the same result as Employee.fullname(self) with the main difference being the inclusion of the self instance when calling the class
>>> 
