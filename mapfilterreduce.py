# numbers = ["2", "7", "27"]
# # print(map(int, numbers))
# numbers = list(map(int, numbers))

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

# numbers[2] = numbers[2] + 1


# print(numbers[2])

# def sq(a):
#     return a * a
#
#
# num = [2, 3, 4, 5, 6, 8, 9, 65, 21]
# square = list(map(sq, num))
# print(square)

# num = [2, 3, 4, 5, 6, 8, 9, 65, 21]
# square = list(map(lambda x: x*x, num))
# print(square)


# def square(a):
#     return a * a
#
#
# def cube(a):
#     return a * a * a
#
#
# func = [square, cube]
# num = [2, 3, 4, 5, 6, 8, 9, 65, 21]
#
# for i in range(7):
#     val = list(map(lambda x: x(i), func))
#     print(val)


# --------------------------FILTER FUNCTION---------------------------
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def is_greater_7(num):
    return num > 7


greater_than_7 = list(filter(is_greater_7, list_1))
print(greater_than_7)

# ----------------------REDUCE FUNCTION---------------------------
from functools import reduce

list1 = [1, 2, 3, 4]

for i in list1:
    num = num + i

print(num)
