class A:
    def met(self):
        print("This Is A Method From Class A")


class B(A):
    def met(self):
        print("This Is A Method From Class B")


class C(A):
    def met(self):
        print("This Is A Method From Class C")


# class D(B, C):
class D(C, B):
    def met(self):
        print("This Is A Method From Class D")


a = A()
b = B()
c = C()
d = D()

d.met()
