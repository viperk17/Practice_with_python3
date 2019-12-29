class Employee:
    no_of_leaves = 8

    def __init__(self, name, asalary, arole):
        self.name = name
        self.salary = asalary
        self.role = arole

    #method
    def print_details(self):
        return f"Name is {self.name}. Salary is {self.salary}. ROle is {self.role}"


# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"

# rohan.name = "Rohan"
# rohan.salary = 5664
# rohan.role = "Student"

# print(Employee.no_of_leaves)
# print(Employee.__dict__)
# Employee.no_of_leaves = 9

print(Employee.no_of_leaves)