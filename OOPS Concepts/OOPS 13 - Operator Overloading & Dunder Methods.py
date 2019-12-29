class Employee:
    no_of_leaves = 8

    def __init__(self, name, asalary, arole):
        self.name = name
        self.salary = asalary
        self.role = arole

    # method
    def print_details(self):
        return f"Name is {self.name}. Salary is {self.salary}. ROle is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    # DUNDER add method and helps in operator overloading
    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    # def __repr__(self):
    #     return f"Employee ('{self.name}', {self.salary}, '{self.role}')"

    # def __str__(self):
    #     return f"The name is {self.name}. Salary is {self.salary}. Role is {self.role}"


emp1 = Employee("Harry", 455, "Programmer")
emp2 = Employee("Rohan", 255, "Cleaner")

print(emp1 / emp2)
print(emp1)

print(str(emp1))
print(repr(emp1))
