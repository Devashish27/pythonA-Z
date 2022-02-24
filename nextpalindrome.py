"""
Author: Tyro
Date: 11-02-2022
Purpose: Learning
"""

# Take the size of test cases from the user
print("Enter the numbers of test cases one by one\n")


# Handling the value error
# try:
#     size = int(input("Enter the size of test cases\n"))
#
# except ValueError:
#     print("Please enter integer digit only")
#     exit()
#
# # Take the input from the use rone by one
# for i in range(size):
#     # Handling the value error
#     try:
#         testPalindrome = int((input("Enter number to check palindrome\n")))
#         palindrome = testPalindrome
#
#         # Checking the number user entered is palindrome or not
#         if str(palindrome) == str(palindrome)[::-1]:
#             print("The number you entered is palindrome\n")
#
#         # Checking next palindrome for the given number
#         elif str(palindrome) != str(palindrome)[::-1]:
#             while True:
#                 palindrome += 1
#
#                 if str(palindrome) == str(palindrome)[::-1]:
#                     print(
#                         f"Next palindrome for {testPalindrome} is {palindrome}\n")
#                     break
#
#         else:
#             print("The number you entered is not palindrome\n")
#
#     except ValueError:
#         print("Please enter integer only\n")


# Another Method..!
# n = int(input("\nHow many inputs?\n"))
#
# while n > 0:
#     a = int(input())
#     b = a
#     c = a
#     n = n-1
#     while True:
#         if c == int(str(b)[::-1]):
#             print(f"Next palindrome for {a} is {b}.")
#             break
#         else:
#             b = b+1
#             c = c+1




# Actual Solution..!
def next_palindrome(n):
    n = n + 1
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == "__main__":

    n = int(input("Enter The Number Of Test Cases: \n"))
    numbers = []

    for i in range(n):
        number = int(input("Enter The Number: \n"))
        numbers.append(number)
    # print(numbers)

    for i in range(n):
        print(f"Next Palindrome for {numbers[i]} is {next_palindrome(numbers[i])}")
