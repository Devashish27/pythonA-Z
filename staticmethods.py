class Employee:
    no_of_leaves = 12

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
        return "Everyone"


tyro = Employee("Tyron Belisario", 342, "Programmer")
ryo = Employee("Ryo Saeba", 547, "Security Engineer")
kishan = Employee.from_dash("Kishan-480-Student")

# print(kishan.salary)
# print(kishan.no_of_leaves)
# print(kishan.printgood("Tyron"))

Employee.printgood("Umibozu!!")
