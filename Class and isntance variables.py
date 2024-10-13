#class and instance variables

class Dog:
    kind = 'canine'    #class variable shared by all instances
    def __init__(self, name):
        self.name = name

dog_1 = Dog('Duke')
dog_2 = Dog('Floky')

#instance variables are unique for each variable

print(dog_1.name)

print(dog_2.kind)

#another example of class and instance variables

class Employee:
    raise_amount = 1.04   #assuming this is the amount by which pay is increased for each employee yearly
    
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.inc =(self.pay*Employee.raise_amount)   #applies the raise_amount to each instance
        #self.pay = int(self.pay*sel.raise_amount) accesses the raise_amount from the instance whereas the Employee.raise_amount checks the class for the attribute

        
        
emp_1 = Employee('Eric', 'Wainaina' , 20000)
emp_2 = Employee('Elvis', 'Njoroge', 25000)

print(emp_1.fullname())

#print(Employee.__dict__)  #shows the attributes contained within the Employee class

print(emp_1.pay)

print(emp_2.pay*Employee.raise_amount) #returns the new pay for emp_2


