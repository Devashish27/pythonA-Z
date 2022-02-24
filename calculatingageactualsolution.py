yearAge = int(input("What's Your Age/Year Of Birth\n"))
isAge = False
isYear = False

if len(str(yearAge)) == 4:
    isYear = True

else:
    isAge = True

if yearAge < 1900 and isYear:
    print("You Seem To Be The Oldest Person Alive: ")
    exit()

if yearAge > 2019:
    print("You Are Not Yet Born: ")
    exit()

if isAge:
    yearAge = 2019 - yearAge

print(f"You Will Be 100 Years Old In {yearAge + 100}")

interestedYear = int(input("Enter The Year You Want To Know Your Age In\n"))

print(f"You Will Be {interestedYear - yearAge} Years Old In {interestedYear}")
