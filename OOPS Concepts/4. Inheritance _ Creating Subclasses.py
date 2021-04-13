'''Inheritance allows us to inherit attributes and methods from the parent class
With the help of the we can create subclass from the parent class and we can over ride
or add completely new functionality without effecting the parent class

Example: Lets create developers and managers for employee class
'''


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


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # to keep things simple
        # or
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manger(Employee):
    # pass list of employees that manager supervises
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)  # to keep things simple
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    # ADD OR REMOVE LIST OF EMPLOYEES
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self):
        for emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev1 = Developer('Prashant', 'Singh', 50000, 'Python')
dev2 = Developer('Test', 'User', 62000, 'Java')

mgr1 = Manger('Sue', 'Smith', 90000, [dev1, dev2])  # supervises dev1
'''
print(mgr1.email)

# mgr1.print_emps()

# mgr1.add_emp(dev2)

mgr1.remove_emp()
mgr1.print_emps()
# print(help(Developer))
# print(dev1.email)
# print(dev1.prog_lang)

# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)
'''
# print(isinstance(mgr1, Manger))
# print(isinstance(mgr1, Employee))
# print(isinstance(mgr1, Developer))

# print(issubclass(Developer, Employee))
# print(issubclass(Manger, Employee))
# print(issubclass(Manger, Developer))
