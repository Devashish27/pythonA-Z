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

    def __add__(self, other):     # This is special method called Dunder method..!
        return self.salary + other.salary

    def __truediv__(self, other):
        # return 356
        return self.salary / other.salary

    def __repr__(self):
        # return self.printdetails()
        # return f"The Name Is {self.name}. Salary is {self.salary} and role is {self.role}"
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return f"The Name Is {self.name}. Salary is {self.salary} and role is {self.role}"

    # def __truediv__(self, other):
    #     return self.salary / other.salary


emp1 = Employee("Tyro", 356, "Gymnastic")
# emp2 = Employee("Ryo", 735, "Musician")


# print(emp1 + emp2)
# print(emp1 / emp2)
# print(emp1)
# print(repr(emp1))
print(str(emp1))
