class Employee:
    no_of_leaves = 12
    var = 24

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


class Player:
    no_of_games = 7
    var = 27

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"The Name Is {self.name}. Game is {self.game}"


# class CoolProgrammer(Employee, Player):
class CoolProgrammer(Player, Employee):

    var = 29
    language = "C++"

    def printlanguage(self):
        print(self.language)


tyro = Employee("Tyron Belisario", 342, "Programmer")
ryo = Employee("Ryo Saeba", 547, "Security Engineer")

kishan = Player("Kishan", ["Football"])
Abhimanya = CoolProgrammer("Abhimanya", ["CoolProgrammer"])

# det = Abhimanya.printdetails()
# Abhimanya.printlanguage()
# print(det)

print(Abhimanya.var)
