# For loops
# list1 = ["Henry", "Beckham", "Totti", "Carlos"]
# list1 = ("Henry", "Beckham", "Totti", "Carlos")
list1 = [["Henry", 1], ["Beckham", 4], ["Totti", 7], ["Carlos", 12]]

dict1 = dict(list1)
# print(dict1)

# print(list1[2], list1[3])

# for item, lollypop in list1:
# for item, lollypop in dict1.items():
#     print(item, "and lolly is: ", lollypop)

# for item in dict1:
#     print(item)

items = [int, float, "Glandior", 2, 6, 7, 12, 63, 147, 36]

for i in items:
    if str(i).isnumeric() and i>6:
        print(i)
