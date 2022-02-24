class A:
    classvar1 = "I am a class variable in class A"

    def __init__(self):
        self.var1 = "I am inside class A's Constructor"
        self.classvar1 = "Instance Variable In Class A"
        self.special = "Special"


class B(A):
    # pass
    classvar1 = "I am in class B"

    def __init__(self):
        self.var1 = "I am inside class B's Constructor"
        self.classvar1 = "Instance Variable In Class B"
        # self.special = "Special"
        super().__init__()
        print(super().classvar1)

a = A()
b = B()

print(b.special, b.var1, b.classvar1)

