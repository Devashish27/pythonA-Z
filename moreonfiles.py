f = open("tyro.txt")

# print(f.tell())  # This will tell where your file pointer is and all....!!
print(f.readline())

# print(f.tell())
print(f.readline())

f.seek(10)  # Seek function can start from anywhere..!

# print(f.tell())
print(f.readline())
f.close()
