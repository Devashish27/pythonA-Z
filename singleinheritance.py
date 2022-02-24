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


class Programmer(Employee):
    no_of_holiday = 15
    def __init__(self, aname, asalary, arole, languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages

    def printprog(self):
        return f"The Programmer's Name Is {self.name}. Salary is {self.salary} and role is {self.role}. The Languages are {self.languages}"


tyro = Employee("Tyron Belisario", 342, "Programmer")
ryo = Employee("Ryo Saeba", 547, "Security Engineer")

kishan = Programmer("Kishan", 574, "Developer", ["Graphic Designer"])
Abhimanya = Programmer("Abhimanya", 786, "Engineer", ["Devops Engineer", "Perl"])

# print(Abhimanya.printprog())
# print(Abhimanya.printdetails())
print(Abhimanya.no_of_holiday)


