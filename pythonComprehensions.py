# ls = []
# for i in range(100):
#     if i % 3 == 0:
#         ls.append(i)

# For list Comprehension Syntax...!
# ls = [i for i in range(100)]
#
# print(ls)

# dict1 = {i:f"item{i}" for i in range(100)}
# dict1 = {i:f"item {i}" for i in range(1, 10001) if i%100==0}
# dict1 = {i:f"Item {i}" for i in range(5)}
#
# dict2 = {value:key for key, value in dict1.items()}
# print(dict1, "\n", dict2)

# dresses = {dress for dress in ["dress1", "dress2", "dress1",
#                                "dress2", "dress1", "dress2"]}   # If you write with [] then it will take all data..

# print(dresses)
# print(type(dresses))

evens = (i for i in range(100) if i%2==0)
# print(type(evens))
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())

# for item in evens:
#     print(item)
