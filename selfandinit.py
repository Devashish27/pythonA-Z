class Employee:
    no_of_leaves = 12

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name Is {self.name}. Salary Is {self.salary} and role is {self.role}"


tyro = Employee("Tyron Belisario", 545, "Graphic Designer")
# ryo = Employee()

# tyro.name = "Tyron Belisario"
# tyro.salary = 645
# tyro.role = "Graphic Designer"
#
# ryo.name = "Ryo Seaba"
# ryo.salary = 847
# ryo.role = "Programmer"

# print(tyro.printdetails())
# print(ryo.printdetails())
# print(ryo.no_of_leaves)

print(tyro.salary)
