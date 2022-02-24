# Extension of FIZZBUZZ
num = 1
fizzcount = 0
buzzcount = 0
fizzbuzzcount = 0

while (num <= 1000):
	if (num % 3 == 0) and (num % 5 == 0):
		print(str(num) + ". FIZZBUZZ!")
		fizzbuzzcount += 1

	elif (num % 3 == 0):
		print(str(num) + ". Fizz!")
		fizzcount += 1

	elif (num % 5 == 0):
		print(str(num) + ". Buzz!")
		buzzcount += 1

	else:
		print(str(num) + ". ")

	num += 1

print("_____________________________")
print("Fizz\t\tBuzz\t\tFIZZBUZZ")
# print(str(fizzcount) + "\t\t" + str(buzzcount) + "\t\t" + str(fizzbuzzcount))

print(str("{:,}" .format(fizzcount)) + "\t\t" + str("{:,}".format(buzzcount)) + "\t\t" + str("{:,}".format(fizzbuzzcount)))

# "{:,}".format(variable)
