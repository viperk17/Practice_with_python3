class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first + '.' + last + '@abc.com'

    @property
    def email(self):  # it takes instance as first arguments
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):  # it takes instance as first arguments
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Employee('{} {} {}'".format(self.first, self.last, self.pay)
