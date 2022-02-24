# Lambda functions or anonymous functions

# def add(a, b):
#     return a + b
#
#
# # minus = lambda x, y: x - y
#
#
# def minus(x, y):
#     return x - y
#
#
# print(minus(12, 7))
def a_first(a):
    return a[1]


a = [[1, 54], [5, 6], [8, 25]]
# a.sort(key=a_first)
a.sort(key=lambda x: x[1])
print(a)
