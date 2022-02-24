# a = input("What Is Your Name!!")
# b = input("How Much Do You Earn!")
#
# if int(b) == 0:
#     raise ZeroDivisionError("B is 0 so stopping the program")
#
# if a.isnumeric():
#     raise Exception("Numbers Are Not Allowed")
#
# print(f"Hello {a}")


# Task- Write About 2 built-in Exceptions...!!
c = input("Enter Your Name: ")
try:
    print(a)

except Exception as e:

    if c == "Tyron":
        raise ValueError("Tyro Is Blocked He is Not Allowed ")

    print("Exception Handled")
