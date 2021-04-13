# This allows us to get our class attri getters setters and deleter functionality.
# Property decorator allows us to define a method

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@abc.com'

    @property
    def email(self):  # it takes instance as first arguments
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):  # it takes instance as first arguments
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp1 = Employee('John', 'Smith')

emp1.first = 'Jim'

print(emp1.first)
# print(emp1.email()) #to access email as an instance, define @property before email method
print(emp1.email)
print(emp1.fullname)

# setter :: Define a setter method
# emp1.fullname = 'Alpha Romeo'
del emp1.fullname
# print(emp1.fullname)
