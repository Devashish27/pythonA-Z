# Your age in 2090 (10Points)
# Take age or year of birth as an input from the user and tell them when will they turn 100 years old (5points)
# Don't use any type of modules like datetime, dateutils (-5points)
# They can then optionally provide a year and your program must tell their age in that year (3points)
# You should be handling all sort of errors like- You are not yet born, You seem to be the oldest person alive (2points)
# You can also handle any other error if posiible

# import time
#
# t = time.localtime()
# current_year = t.tm_year
#
#
# def age_calculator(age_or_yearofbirth):
#     if age_or_yearofbirth < 100:
#         print(
#             f"You will turn at age of 100 after {100 - age_or_yearofbirth} years at {100 - age_or_yearofbirth + current_year - age_or_yearofbirth} year")
#
#     elif age_or_yearofbirth == 100:
#         print(f"You already at 100 year age. Congrats.")
#
#     elif age_or_yearofbirth > current_year:
#         print(f"You haven't born yet.")
#
#     elif age_or_yearofbirth > 100 and age_or_yearofbirth < 150:
#         print("You already crossed 100 age. And you are preety old now.")
#
#     elif age_or_yearofbirth > 1000:
#         print(
#             f"You will turn at age of 100 on {100 + age_or_yearofbirth} year and your current age is {current_year - age_or_yearofbirth}.")
#
#     else:
#         print("Invalid input. PLease try again")
#
#
# def age_calculator2(age_or_year, user_year):
#     if age_or_year == 100 or age_or_year < 100:
#         if current_year - age_or_year > user_year:
#             print("Please enter a valid desired year.")
#         elif current_year - age_or_year < user_year:
#             print(f"Your age at year {user_year} will be {user_year - (current_year - age_or_year)}")
#
#     elif age_or_year == 1000 or age_or_year > 1000:
#         print(f"Your age at year {user_year} will be {user_year - age_or_year}")
#
#     elif age_or_year > 5000:
#         print("You are too ahead in future. Please enter desired year between 1000-5000years")
#
#     elif age_or_year < 1000:
#         print("You gone too backward in past. Please enter desired year between 1000-5000years")
#
#     else:
#         print('Invalid input. Please try again')
#
#
# if __name__ == '__main__':
#     print(
#         "Welcome to your age at any year.\nEnter 1 - when you will be 100 year old , 2 - Your age at any year you "
#         "want and 3 to exit the program")
#     while True:
#         choice = int(input("Enter your choice here : "))
#         if choice == 1:
#             Age_or_Yearofbirth = int(input("Please Enter your 'age' or 'year of birth' here : "))
#             age_calculator(Age_or_Yearofbirth)
#         elif choice == 2:
#             Age_or_Yearofbirth = int(input("Please Enter your 'age' or 'year of birth' here : "))
#             user_year = int(input("Enter your desired year : "))
#             age_calculator2(Age_or_Yearofbirth, user_year)
#         elif choice == 3:
#             print("Thanks to use Your age in any year.")
#             exit()
#         else:
#             print("Invalid choice. Please try again with a valid one")


# Another Method -2
# print("press 1 for knowing when your are getting 100 years.")
# print("press 2 for what your age will be in following year.")
# a = int(input())
#
# if a == 1:
#     age = int(input("write your current age :"))
#     year = int(input("write the current year :"))
#
#     if(year < 2019):
#         print("you are not born yet")
#
#     elif(age < 100):
#         b = 100 - age
#         c = b + age
#         print(f"In {year+b} your age will be: ", c)
#
# elif a == 2:
#     age = int(input("write your current age :"))
#     year = int(input("write the current year :"))
#
#     if(year < 2019):
#         print("you are not born yet")
#
#     if year >= 2019:
#         particular_year = int(input("for knowing your age in that particular year write full year:"))
#         c = age + (particular_year - year)
#         print(f"your age in {particular_year} will be {c}")
#         # age stored in file
#         with open("list_of_ages.txt", "a") as f:
#             f.write(f"{str(c)} \n")


# Method -3:
# Take age or year of birth as an input from the user. Store the input in one variable.
# Your program should detect whether the entered input is age or year of birth
# and tell the user when they will turn 100 years old. (5 points).
#
# Here are a few instructions that you must have to follow:
#
# Do not use any type of modules like DateTime or date utils. (-5 points)
# Users can optionally provide a year, and your program must tell their age in that particular year. (3points)
# Your code should handle all sort of errors like:                       (2 points)
# You are not yet born
# You seem to be the oldest person alive
# You can also handle any other errors, if possible!

# a = int(input("Enter DOB or age: "))
# _type = "INVALID"
# if a >= 1900:
#     _type = "DOB"
#     if a > 2021:
#         print("You aren't born yet !")
#         exit()
# elif a <= 100:
#     _type = "AGE"
# else:
#     if a < 1900:
#         print("You seem to be oldest person alive !")
#         exit()
#     else:
#         raise ValueError("Not a valid age or DOB")
#
# if _type == "DOB":
#     DOB = a
# else:
#     DOB = 2021 - a
# print("You will turn 100 in", DOB + 100)
#
#
# year = input("Enter a year if you want(otherwise type none): ")
#
# if year.lower() == "none":
#     exit()
#
# if DOB > int(year):
#     raise ValueError(f"You were not born in {year}")
# elif int(year)-DOB > 100:
#     print("You won't survive in", year)
# else:
#     print(f"You will turn {int(year) - DOB} in {year}")
#



# Method-4 sIMPLE
a = int(input("Enter the current year: "))
b = int(input("Enter your current age: "))
if a == 2090:
    print(f"Your age is {b}")
elif a>2090:
    print("Please enter a year less than 2090")
c = 2090 - a
print(f"Your age in 2090 will be: {b+c}")
