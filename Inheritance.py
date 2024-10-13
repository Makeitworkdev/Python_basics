#inheritance of class attributes and methods

class Employee:
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first =  first
        self.last = last
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = (self.pay*self.raise_amount)

class Developer(Employee):  #a subclass that inherit's the Employee class attributes and methods
    pass  #for when no chnage is to be made to the attributes and methods of the parent class

emp_1 = Employee('James', 'John', 30000)
emp_2 = Developer('June', 'Journey', 32000)

print(emp_1.fullname())

print(emp_2.pay)  #pay before raise

emp_2.apply_raise()

print(emp_2.pay)  #pay after raise
#it is clear that the Developer subclass uses the methods from the parent class Employee

class Manager(Employee):
    def __init__(self, first, last, pay, in_charge_of):
        super().__init__(first, last, pay)    #the super method is used to inherit the parent class attributes and methods without having to set them for the subclass itself
        self.in_charge_of = in_charge_of

mgr_1 = Manager('Joyce', 'Njuguna', 40000, 'Human_resources')

print(mgr_1.fullname())

mgr_1.apply_raise()
print(mgr_1.pay)

print(mgr_1.in_charge_of)



