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


tyro = Employee("Tyron Belisario", 342, "Programmer")
ryo = Employee("Ryo Saeba", 547, "Security Engineer")

# tyro = Employee()
# ryo.name = "Ryo Saeba"
# ryo.salary = 342
# ryo.role = "Programmer"
#
# tyro.name = "Tyron Belisario"
# tyro.salary = 547
# tyro.role = "Security Engineer"

# print(tyro.salary)
# Employee.no_of_leaves = 53

tyro.change_leaves(86)   # If you want to take instance class but don't want to consider self then we can use
# ------>This Method Above Mentioned<-------.
# Employee.change_leaves(86)
print(tyro.no_of_leaves)
