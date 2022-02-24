# Using python 2.7
# n=input('Enter number of apples present : ')
# mn=input('Enter min value of range : ')
# mx=input('Enter max value of range : ')
#
# if mn==mx:
#     print 'range is not valid'
# else:
#     for i in xrange(mn,mx+1):
#         if n%i==0:
#             print '{} is a divisor of {}'.format(i,n)
#         else:
#             print '{} is not a divisor of {}'.format(i,n)
#

# Other method correct way
# n = int(input("enter the number of apples"))
# mn = int(input("enter the minimum range"))
# mx = int(input("enter the maximum range"))
# for i in range(mn, mx + 1):
#     if mn == mx:
#         print("range is not defined. Mx=Mn")
#     if n % i == 0:
#         print(f"{n} is divisible with {i}")
#     else:
#         print(f"{n} is not divisible with {i}")



# Original Answer...
apples = int(input("Enter The Number Of Apples: \n"))
mn = int(input("Enter The Minimum Number To Check: \n"))
mx = int(input("Enter The Maximum Number To Check: \n"))

for i in range(mx, mn + 1):
    if apples % i == 0:
        print(f"{i} is a divisor of {apples}")
    else:
        print(f"{i} is not a divisor of {apples}")
