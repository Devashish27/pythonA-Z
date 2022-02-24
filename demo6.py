# Swapping two numbers..!
a = 2
b = 7

# Method-1
# c = a
# a = b
# b = c

# Method-2
# a = a + b
# b = a - b
# a = a - b

# Method-3 using xor which will save memory..!
# a = a ^ b
# b = a ^ b
# a = a ^ b

# Method-4
a, b = b, a 

print(a)
print(b)
