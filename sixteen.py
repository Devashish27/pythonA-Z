# Guess the random number...!
n = 27
number_of_guesses = 1
print("Number of guesses is limited to only 9 times.!")

while number_of_guesses <= 9:
    guess_number = int(input("Guess the number :\n"))

    if guess_number < 27:
        print("You enter less number please input greater number..\n ")
    elif guess_number > 27:
        print("You enter greater number please enter smaller number..\n")
    else:
        print("You won\n")
        print(number_of_guesses, "Number of guess you took to finish..!")
        break
    print(9-number_of_guesses, "Number of guesses left")
    number_of_guesses = number_of_guesses + 1

if number_of_guesses > 9:
    print("Game Over!!")
