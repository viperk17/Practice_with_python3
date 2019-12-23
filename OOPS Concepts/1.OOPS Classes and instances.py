class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+ last + '@abc.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp1 = Employee('Prashant','Singh',40000)
emp2 = Employee('Alpha','Singh', 50000)

# print(emp1)
# print(emp2)

# print(emp1.email)
# print(emp2.email)

#run using class
emp1.fullname()
print(Employee.fullname(emp1))



#for full name
# print('{} {}'.format(emp1.first, emp1.last))

# print(emp1.fullname())

'''To input data normally'''
# emp1.first = 'Prahant'
# emp1.last = 'Singh'
# emp1.email = 'prashant.singh@abc.com'
# emp1.pay = 40000
#
# emp2.first = 'Alpha'
# emp2.last = 'Singh'
# emp2.email = 'Alpha.singh@abc.com'
# emp2.pay = 60000


