import operator

d = {1: 2, 2: 3, 3: 4, 2: 1, 4: 5}
print('Original dictionary: ', d)

sorted_dict = sorted(d.items(), key=operator.itemgetter(1))
print('Dictionary in Ascending Order by value: ', sorted_dict)

sorted_dict = dict(sorted(d.items(), key=operator.itemgetter(1).reverse))
print('Dictionary in Descending Order by value: ', sorted_dict)
