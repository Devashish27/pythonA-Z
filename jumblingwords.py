# Method - 1:
# def jumbleNames(cNames):
#     # This is a function to Jumble Up the Names & Surnames
#     split_names = []
#     split_surnames = []
#     for names in cNames:
#         cNamesSplit = names.split(" ", 1)          # Splitting each cName into 2 parts
#         split_names.append(cNamesSplit[0])      # Creating a list of only names
#         split_surnames.append(cNamesSplit[1])   # Creating a list of only surnames
#         split_surnames.reverse()                # Reversing the surname list inside the loop
#
#     # Now creating the final list of JumbledUp Names & Surnames
#     cJumbleNames = []
#     for i in range(len(cNames)):
#         cJumbleNames.append(split_names[i] + " " + split_surnames[i])
#
#     return cJumbleNames
#
#
# if _name_ == '__main__':
#     cNames = []
#     n = int(input("How many number of names to input? "))
#     for i in range(n):
#         cNames.append(input(f"{i+1}. Enter one name & Surname: "))
#     print("Original List of Names:", cNames)
#
#     cJumbleNames = jumbleNames(cNames)
#     print("Jumbled List of Names :", cJumbleNames)



# Method - 2:
# import random
#
#
# def jumble_names():
#     # If maxsplit is specified, the list will have the maximum of maxsplit+1 items.
#     # Thus in case of lname, even if someone has specified middle name it'll be considered as a whole
#     fname = [name.split()[0] for name in names]
#     lname = [name.split(" ", 1)[1] for name in names]
#
#     for _ in names:
#         random_fname = random.choice(fname)
#         random_lname = random.choice(lname)
#
#         print(f"{random_fname} {random_lname}")
#
#         fname.remove(random_fname)
#         lname.remove(random_lname)
#
#
# if _name_ == '__main__':
#     n = int(input("Enter number of friends: "))
#     names = []
#     for i in range(n):
#         names.append(input("Enter name of your friend: "))
#
#     jumble_names()




# Method -3 :
# import random
#
# if __name__=='__main__':
#     number=int(input("How many names you want to enter\n"))
#     names_list=[input("Enter the name") for i in range(number)]
#     print(names_list)
#
#     # initializing the list
#     list1=[]
#     list2=[]
#     list3=[]
#
#     # this will split each list item and store it in a list
#     list1=[i.split(" ") for i in names_list]
#     # print(list1)
#
#     # this will split first name and store it in a list
#     list2=[i[0] for i in list1]
#     # print(list2)
#
#     # this will split last name and store it in a list
#     list3=[i[1] for i in list1]
#     # print(list3)
#
#     for i in range(len(list2)):
#         print(list2[i]+random.choice(list3))

        