class Employee:
    no_of_leaves = 12
    var = 24
    _protec = 45
    __private = 12

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name Is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This Is Good " + string)


emp = Employee("Tyro", 462, "Lazy-Programmer")
# print(emp._protec)
print(emp._Employee__private)
