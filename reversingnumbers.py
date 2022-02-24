# Method -1
# a = sorted(list(map(int, input().split())))
# print(a[::-1])
# print(list(reversed(a)))
# for i in range(len(a) // 2):
#     a[i], a[-(i + 1)] = a[-(i + 1)], a[i]
# print(a)


# Other Method - 2:
# lst = [int(input("Enter the list Element:\n")) for i in range(3)]
# print(f"Your list is {lst}")
# while True:
#     choice1 = int(input("Enter 1(Traditional Method),2(Slicing Method) or 3(Swaping Method) for reverse the List:\n"))
#     if choice1 == 1:
#         lst1 = lst[:]
#         lst1.reverse()
#         print("The Answer of First Method is :",lst1)
#     elif choice1 == 2:
#         lst2 = lst[::-1]
#         print("The Answer of Second Method is :", lst2)
#     elif choice1 == 3:
#         for i in range(len(lst)//2):
#             lst[i], lst[len(lst)-i-1] = lst[len(lst)-i-1], lst[i]
#         print("The Answer of Third Method is :", lst)
#     choice2 = input("C for Continue and Q for Quit:\n")
#     if choice2.capitalize() == 'Q':
#         break
#     if choice2.capitalize() == 'C':
#         continue
# print("Thank You.")


# Actual Answer..
# Take The Size From User..!

print("Enter the numbers in list one by one: \n")
size = int(input("Enter The Size Of List: \n"))

# Initialize a blank list..!
mylist = []

# Take Input From User One By One..!
for i in range(size):
    mylist.append(int(input("Enter THe List Element: \n")))


# mylist = [4, 6, 2, 8, 1]
print(f"Your List is {mylist}\n")

reverse1 = mylist[:]  # Here this [:] tAKES a copy of list. so that values change and stored inside mylist copy
reverse1.reverse()

reverse2 = mylist[::-1]

print(f"My First Reverse List of {mylist} Is {reverse1}: ")
print(f"My Second Reverse List of {mylist} Is {reverse2}: ")

reverse3 = mylist[:]
for i in range(len(reverse3)//2):
    reverse3[i], reverse3[len(reverse3) - i - 1] = reverse3[len(reverse3) - i - 1], reverse3[i]

    print(f"The Reversed List At i={i} is {reverse3}")

print(f"My Third Reverse List of {mylist} Is {reverse3}: ")

if reverse1 == reverse2 and reverse2 == reverse3:
    print("All Three methods give same result...")
