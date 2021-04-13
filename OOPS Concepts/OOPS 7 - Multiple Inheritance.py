class Employee:
    var = 8
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


############### Multiple Inheritance #########################
class Player:
    var = 9
    no_of_games = 4

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def print_details(self):
        return f"The name is {self.name}. Game is {self.game}"


class Cool_Programer(Employee, Player):
    language = "C++"

    def print_language(self):
        print(self.language)


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 4215, "Student")

shubham = Player("Shubham", ["Cricket"])
karan = Cool_Programer("Karan", 99999, "CoolProgrammer")

print(karan.print_details())

print(karan.var)
