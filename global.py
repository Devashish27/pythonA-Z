# l = 10  # Global
#
#
# def function1(n):
#     # l = 5  # Local
#     m = 7  # local
#     global l
#     l = l + 45
#     print(l, m)
#     print(n, "I have printed")
#
#
# function1("This is me!!")
# print(l)

x = 66
def dev():
    x = 20

    def ramkrish():
        global x
        x = 63

    print("Before calling ramkrish()", x)
    ramkrish()
    print("After calling ramkrish()", x)
    # print(x)


dev()
print(x)
