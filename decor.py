# def function1():
#     print("Subscribe Now!!")
#
#
# func2 = function1
# del function1
# func2()

# def funcret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         # return int
#         return sum
#
#
# a = funcret(1)
# # a = funcret(0)
# print(a)

# def executor(func):
#     func("Hello")
#
#
# executor(print)

def dec1(func1):
    def nowexec():
        print("Executing now!!")
        func1()
        print("Executed!!")

    return nowexec

@dec1
def who_is_tyro():
    print("Tyro Is A Good Man")


# who_is_tyro = dec1(who_is_tyro)

who_is_tyro()
