print("Enter Num 1\n")
# num1 = int(input())
num1 = input()

print("Enter Num 2\n")
# num2 = int(input())
num2 = input()

try:
    print("The Sum Of These Two Numbers Is", int(num1) + int(num2))

except Exception as e:
    print(e)

print("This line is very important")