class Employee:
    num_of_emps = 0  # counts no of employees

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@abc.com'

        Employee.num_of_emps += 1  # counts no of employees

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp1 = Employee('Prashant', 'Singh', 50000)
emp2 = Employee('Test', 'User', 62000)

# Employee.raise_amount = 1.05    #changed rate

print(Employee.num_of_emps)

# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)

# prints all information as dictionary
# print(emp1.__dict__)
# to print the output normally before declaring raise_amount in function:
''' def apply_raise(self):
        self.pay = int(self.pay * 1.04)
'''
# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)
#
# print(emp2.pay)
# emp2.apply_raise()
# print(emp2.pay)
