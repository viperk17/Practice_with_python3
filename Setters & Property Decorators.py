class Employee:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@code.com"

    @property
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        return f"{self.fname}.{self.lname}@code.com"

    # to set email using setter and getter. Create setter using decorator
    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]


Knight_Alpha = Employee("Knight", "Alpha")
Alfa_Romeo = Employee("Alfa", "Romeo")
print(Knight_Alpha.email)
Knight_Alpha.fname = "APL"

print(Knight_Alpha.email)
Knight_Alpha.email = "this.that@gmail.com"
print(Knight_Alpha.email)


