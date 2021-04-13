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


############### Single Inheritance #########################
class Programmer(Employee):

    # constructor
    def __init__(self, name, asalary, arole, language):
        # super().__init__(name, asalary, arole)
        self.name = name
        self.salary = asalary
        self.role = arole
        self.language = language

    def print_prog(self):
        return f"Programmer's Name is {self.name}. Salary is {self.salary}. ROle is {self.role}. Languages are {self.language}"


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 4215, "Student")

shubham = Programmer("Shubham", 727, "Programmer", "Python")
karan = Programmer("Karan", 999, "Programmer", ["Python", "CPP"])
print(karan.print_prog())
print(karan.print_details())
