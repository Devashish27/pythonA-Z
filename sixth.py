# Sets in Python...!
s = set()
# print(type(s))

# s_from_list = set([1, 2, 3, 4])
# print(s_from_list)
# print(type(s_from_list))

s.add(1)
s.add(2)
# s1 = s.union({1, 2, 3})
# s1 = s.intersection({1, 2, 3})  # This takes only common values...!
# print(s1, s)
s.remove(2)

s1 = {4, 6}
# print(s.isdisjoint(s1))
print(s)
