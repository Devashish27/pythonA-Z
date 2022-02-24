# While loops..
# i = 0
#
# # while i < 26:
# while True:  # This will keeps on running.
#     if i+1 < 5:
#         i = i + 1
#         continue
#     # print(i+1)
#     # If you want in row then use,
#     print(i + 1, end=" ")
#     if i==55:
#         break  # Stop loop...
#     i = i + 1

# Eg:
while(True):
    inp = int(input("Enter a number: \n"))
    if inp>100:
        print("Congrats man you have entered a number greater than 100..\n")
        break
    else:
        print("Try again!!\n")
        continue
