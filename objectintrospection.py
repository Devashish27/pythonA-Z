class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codealongsidetyro.com"

    def explain(self):
        return f"This Employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email Is Not Set. Please Set It Using Setter..!"
        return f"{self.fname}.{self.lname}@codealongsidetyro.com"

    @email.setter
    def email(self, string):
        print("Setting Now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


skillf = Employee("Skill", "F")
# print(skillf.email)

# print(type(skillf))
# print(type("This Is A String!!"))
# print(id("This Is A String!!"))    # Here, Id is stored differently for all string variables..!

o = "This Is A Sentense"
# print(dir(o))
# print(dir(skillf))

import inspect
print(inspect.getmembers(skillf))
