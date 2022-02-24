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


dev_labs = Employee("Devarkonda", "Labs")
vishn_shiv = Employee("Vishn", "Shiv")

# print(dev_labs.explain())
print(dev_labs.email)

dev_labs.fname = "US"

print(dev_labs.email)  # If you want to call this print without brackts like this '()' then you have to use
# @property decorator thing.

dev_labs.email = "kehaf.rsjbf@gmail.com"
# print(dev_labs.fname)
# print(dev_labs.lname)
print(dev_labs.email)


# For deleting email..!
del dev_labs.email

print(dev_labs.email)
dev_labs.email = "Volwes.Vagon@gmail.com"
print(dev_labs.email)
