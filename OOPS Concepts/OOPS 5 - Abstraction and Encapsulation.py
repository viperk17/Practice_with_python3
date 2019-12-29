# Encapsulation : Showing the necessary details and hiding the background information
# Hiding the implementation.

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

    @classmethod
    def from_str(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))

    @staticmethod
    def print_good(string):
        print("This is good " + string)


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 4215, "Student")
karan = Employee.from_str("Karan-450-Student")
