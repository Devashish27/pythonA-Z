# Method - 1:

# num = 1

# while (num <= 100):
	
# 	if (num % 3 == 0) and (num % 5 == 0):

# 		print(str(num) + ". FIZZBUZZ!!")

# 	elif (num % 3 == 0):

# 		print(str(num) + ". FIZZ!")

# 	elif (num % 5 == 0):

# 		print(str(num) + ". BUZZ!")

# 	else:

# 		print(str(num) + ".")

# 	num += 1



# Method - 2:

# for i in range(1, 101):

# 	if (i % 3 == 0) and (i % 5 == 0):

# 		print(i, ": FizzBuzz!")

# 	elif (i % 3 == 0):

# 		print(i, ": Fizz!")

# 	elif (i % 5 == 0):

# 		print(i, ": Buzz!")

# 	else:

# 		print(i, ":")



# Method - 3:

for fz in range(0,51):
	
	if(fz%15==0):
		
		print(fz,'Fizzbuzz')
	
	elif(fz%3==0):
		
		print(fz,'Fizz')
	
	elif(fz%5==0):
		
		print(str(fz)+' Buzz')
	
	else:
		
		print(fz)
		