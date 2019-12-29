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
        if self.fname == None or self.lname == None:
            return "Email not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@code.com"

    # to set email using setter and getter. Create setter using decorator
    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


skillf = Employee("Skill", "F")
print(skillf.email)

# print(type(skillf))
# print(type("this is a string"))
# print(id("this is a string"))
# print(id("that that"))
#
# # print(dir(0))
# print(dir(skillf))

import inspect

print(inspect.getmembers(skillf))   #inspecting the members
