class Employee:
    num_of_emps = 0  # counts no of employees
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@abc.com'

        Employee.num_of_emps += 1  # counts no of employees

    def fullname(self):  # it takes instance as first arguments
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    '''Since self takes instance as first argument. We can change it, it will take
    class as first argument. We gonna use class method & return a regular method
    into class method. ITs easy as adding a decorator to the top called #@classmethod'''

    # now cls method as first argument
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # dont havee to parse the string every time new emp is created
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# Regular method auto pass instance as first argument eg. self
# Class method auto pass instance as first argument eg. cls
# Static method dont pass anything automatically. Dont pass instance for the class
#
# Example: Lets take a simple func that take in a date and return whether or not it
# is a workday. It doesnt depend on any specific instance or class variable.
#
# We are gonna make static method and a decorator

emp1 = Employee('Prashant', 'Singh', 50000)
emp2 = Employee('Test', 'User', 62000)

import datetime

my_date = datetime.date(2019, 12, 24)

print(Employee.is_workday(my_date))

# can run class method using the instance and it will change the value of cls var and instance amount to 5%
# emp1.set_raise_amt(1.05)    #changed value to 5%

# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)
#
# emp_str1 = 'John-Doe-70000'
# emp_str2 = 'Steve-Smith-30000'
# emp_str3 = 'Jane-Doe-90000'

# #The user dont have to parse the value every time new emp is created
# new_emp1 = Employee.from_string(emp_str1)
#
# first, last, pay = emp_str1.split('-')
# new_emp1 = Employee(first,last,pay)

# print(new_emp1.email)
# print(new_emp1.pay)
