# Method-1
# Here if number is greater than 10 then it should be added by 1 to itself...

# Input:
# [1, 6, 87, 43]
#
# Output:
# [1, 6, 88, 44]

# def nextPalindromeIf(n):
#     temp = n
#     if n > 10:
#         while 1:
#             if str(n) == str(n)[::-1]:
#                 return n
#             n += 1
#     else:
#         return temp
#
#
# no_of_cases = int(input("Enter the no of test cases: "))
# cases = [int(input(f"Enter a number at index {i}: ")) for i in range(no_of_cases)]
#
# palindromeLst = [nextPalindromeIf(item) for item in cases]
# cases = palindromeLst  # as per question
# print(cases)


# Method - 2:
# x=[]
# r=[]
# try:
#     n=int(input("How much number you want to insert in list \n"))
#     for i in range(n):
#         t=int(input("Please input the numbers "))
#         x.append(t)
#         if t>10:
#             while True:
#                 t=t+1
#                 p=str(t)
#                 if p==p[::-1]:
#                     r.append(p)
#                     break
#                 else:
#                     continue
#         else:
#             r.append(t)
#     print(r)
# except Exception as e:
#     print(e)


# Original Answer..
def next_palindrome(n):
    n = n + 1
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == "__main__":
    size = int(input("Enter The Size Of Your List: \n"))
    num_list = []
    for i in range(size):
        num_list.append(int(input("Enter The Number Of The List: \n")))
    print(f"You Have Entered {num_list}")

    print(f"Output List:  {[num_list[i]if num_list[i] < 10 else next_palindrome(num_list[i])for i in range(size)]}")

    # new_list = []
    # for element in num_list:
    #     if element > 10:
    #         n = next_palindrome(element)
    #         new_list.append(n)
    #
    #     else:
    #         new_list.append(element)
    # print(f"Output List:  {new_list}")
