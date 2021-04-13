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


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 4215, "Student")


harry.change_leaves(22)
print(harry.no_of_leaves)

