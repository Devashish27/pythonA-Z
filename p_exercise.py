# pickle
# Use Requests Module To Download The Iris Dataset
# import pickle
#
# import requests
#
# data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
# # print(data)
#
# l1 = data.split("\n")
# # print(l1)
#
# l2 = [item.split(",") for item in l1 if len(item) != 0]
# print(l2)
#
# with open("myiris.pkl", "wb") as f:
#     pickle.dump(l2, f)

# To Read The Pickle You Can Use This Code...
# import pickle
#
# with open("iris.pkl", "rb") as f:
#     print(pickle.load(f))
