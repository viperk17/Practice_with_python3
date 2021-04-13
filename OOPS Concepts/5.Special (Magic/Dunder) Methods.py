# Dunder/ Magic
"""Allow us to implement operator overloading.
These are always surrounded by double underscores (__)"""


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

    # add two employees together, we are gonna create dunder add method
    def __add__(self, other):
        return self.pay + other.pay

    # '''Dunder'''
    # used for debugging and logging errors
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    # is ment to be more readable representation of an object for an end user
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __len__(self):
        return len(self.fullname())


emp1 = Employee('Prashant', 'Singh', 50000)
emp2 = Employee('Test', 'User', 62000)
"""
When we run repr or str it return vague objects
eg: 
print(emp1)
repr(emp1)
str(emp1)
OUPUT: <__main__.Employee object at 0x7f2ab1d29860>
To fix this we will se def __repr__ & __str__
"""
# print(emp1)
print(repr(emp1))
print(str(emp1))
# similar to below
# print(emp1.__repr__())
# print(emp1.__str__())
#
# # print(len('test')) #or print('test'.__len__())
# print(len(emp1))
# print(emp1 + emp2)  # dunder __add__ method
#
# # print(1 + 2)
#
# print(int.__add__(1, 4))
# print(str.__add__('a', 'v'))
