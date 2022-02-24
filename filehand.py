# Opening the image..!
f = open(r'C:\Users\AYeddula\OneDrive - DXC Production\Desktop\images\spice-wolf.jpeg', 'rb')  # Read-Binary = rb

f1 = open(r'C:\Users\AYeddula\OneDrive - DXC Production\Desktop\Pythonlang\MyPic.jpeg', 'wb')  # Copying into another file

for i in f:
	f1.write(i)

#for i in f:
#	print(i)

# f = open('demo.txt', 'r')

# f1 = open('demo1.txt', 'w')  # Write

# for data in f:
# 	f1.write(data)

# f1 = open('demo1.txt', 'a')  # Appending the text

# f1.write("Something ")
# f1.write("girl ")
# f1.write('Laptop ')

# print(f.read())  # For reading entire file..

# print(f.readline(4), end="#")  # This will print first line
# print(f.readline())  # Read second line.
 
