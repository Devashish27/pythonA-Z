print("Pattern Printing..!")
num = int(input("Enter Num How Many Rows You Want: "))
print("Enter 1 or 0")
bool_val = input("1 for True value or 0 for False: ")

if bool_val == "1":
    for i in range(0, num + 1):
        print("*" * i)

if bool_val == "0":
    for i in range(num, 0, -1):
        print("*" * i)
