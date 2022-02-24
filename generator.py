"""

Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -

"""


def gen(n):
    for i in range(n):
        yield i
        # return i

# for i in range(46):
#     print(i)


g = gen(2)
# print(g)
# print(g.__next__())
# g.__next__()
# print(g.__next__())
# print(g.__next__())

# for i in g:
#     print(i)

t = "tyro"
# print(t[0])
# print(iter(t))
ier = iter(t)
print(ier. __next__())
print(ier. __next__())


# for c in t:
#     print(c)
