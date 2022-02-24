import random


def guessGame(a, b, actual):
    guess = int(input(f"Guess A Number Between {a} and {b}\n"))
    nguess = 1

    while guess != actual:
        if guess < actual:
            guess = int(input(f"Enter A Bigger Number\n"))
            nguess += 1

        # elif guess > actual:
        else:
            guess = int(input(f"Enter A Smaller Number\n"))
            nguess += 1

    print(f"You Guessed The Number In {nguess} guesses\n")
    return nguess


if __name__ == "__main__":
    a = int(input("Enter The Value Of a: \n"))
    b = int(input("Enter The Value Of b: \n"))

    actual1 = random.randint(a, b)
    print("Player 1's Turn\n")
    g1 = guessGame(a, b, actual1)

    print("Player 2's Turn\n")
    actual2 = random.randint(a, b)
    g2 = guessGame(a, b, actual2)

    if g1 < g2:
        print("Player 1 is winner!\n")

    elif g1 > g2:
        print("Player 2 is winner!\n")

    else:
        print("Its a tie!!\n")

    print(f"The Number For Player 1 was {actual1} and for player 2 was {actual2}")
