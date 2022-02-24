class Employee:
    no_of_leaves = 7
    pass


tyro = Employee()
ryo = Employee()

tyro.name = "Tyron Belisario"
tyro.salary = 645
tyro.role = "Graphic Designer"

ryo.name = "Ryo Seaba"
ryo.salary = 847
ryo.role = "Programmer"

# print(tyro.name)
# print(tyro.no_of_leaves)
# print(ryo.no_of_leaves)
print(Employee.no_of_leaves)
Employee.no_of_leaves = 12
# print(ryo.__dict__)
print(Employee.__dict__)

# ryo.no_of_leaves = 12
# print(ryo.__dict__)
print(Employee.__dict__)
print(Employee.no_of_leaves)

# Instances and Classes Can't Be Changed...!!
