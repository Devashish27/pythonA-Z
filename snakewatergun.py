# Eg-1:
# import random
#
# n = input('Enter your name : ')
# print('Welcome to our game ', n, '- Snake Water Gun')
# r = int(input('Enter the number of rounds you wants to play : '))
# rounds = 1
# options = ['s', 'w', 'g']
# player_win = 0
# computer_win = 0
#
# while rounds <= r:
#     print(f"Round : {rounds}")
#     print("Hit 's' for snake , Hit 'g' for gun , Hit 'w' for water")
#     player = input('Choose your option : ')
#     if player != 's' and player != 'g' and player != 'w':
#         print('Invalid input! Please enter again')
#         continue
#     computer = random.choice(options)
#
#     if computer == 's':
#         if player == 'g':
#             player_win += 1
#         elif player == 'w':
#             computer_win += 1
#
#     if computer == 'g':
#         if player == 'w':
#             player_win += 1
#         elif player == 's':
#             computer_win += 1
#
#     if computer == 'w':
#         if player == 's':
#             player_win += 1
#         elif player == 'g':
#             computer_win += 1
#
#     if player_win > computer_win:
#         print('Congarts!You win in this round', n)
#     elif player_win < computer_win:
#         print('Oops!You lose in this round', n)
#         print('Better luck next time')
#     else:
#         print('Round draw!', n)
#
#     rounds += 1
#
# if player_win > computer_win:
#     print('Congrats!You win the game', n)
# elif player_win < computer_win:
#     print('Oops!You lose the game', n)
# else:
#     print('Match draw!', n)
# print('Your score : ', player_win)
# print('Computer score : ', computer_win)


# EG-2:
# import random
# list = ["Snake", "Water", "Gun"]
# choice = random.choice(list)
#
# def won():
#     if i == 1:
#         print("You won the ", i, "st game")
#     elif i == 2:
#         print("You won the ", i, "nd game")
#     elif i == 3:
#         print("You won the ", i, "rd game")
#     else:
#         print("You won the ", i, "th game")
#     return i+1
#
# def loose():
#     if i == 1:
#         print("You loose the ", i, "st game")
#     elif i == 2:
#         print("You loose the ", i, "nd game")
#     elif i == 3:
#         print("You loose the ", i, "rd game")
#     else:
#         print("You loose the ", i, "th game")
#     return i+1
#
# def draw():
#     if i == 1:
#         print("You draw the ", i, "st game")
#     elif i == 2:
#         print("You draw the ", i, "nd game")
#     elif i == 3:
#         print("You draw the ", i, "rd game")
#     else:
#         print("You draw the ", i, "th game")
#     return i+1
#
# sum = 0
# add = 0
#
#
#
#
#
# print("Let's play a game whose name is: Snake Water Gun:\nYou have to play 9 times: ")
#
# i = 1
# while i<10:
#     print("Press:\n s for snake\n w for water\n g for gun: ")
#     a = input()
#     if a=="s":
#         if choice=="Snake":
#             print("You draw the game with the computer")
#             print(draw())
#             a = 1
#             i=i+1
#
#         elif choice=="Water":
#             print("You won the game as snake drank the water")
#             print(won())
#             a = 2
#             i = i + 1
#         else:
#             print("You loose the game as snake has been killed by the gun")
#             print(loose())
#             a = 3
#             i = i + 1
#     elif a=="w":
#         if choice == "Water":
#             print("You draw the game with the computer")
#             print(draw())
#             a = 1
#             i = i + 1
#         elif choice == "Snake":
#             print("You loose the game as snake drank the water")
#             print(loose())
#             a = 3
#             i = i + 1
#         else:
#             print("You won the game as gun sank in the water")
#             print(won())
#             a = 2
#             i = i + 1
#     elif a=="g":
#         if choice == "Gun":
#             print("You draw the game with the computer")
#             print(draw())
#             a = 1
#             i = i + 1
#         elif choice == "Snake":
#             print("You won the game as snake has been killed by the gun")
#             print(won())
#             a = 2
#             i = i + 1
#         else:
#             print("You loose the game as gun sank in the water")
#             print(loose())
#             a = 3
#             i = i + 1
#     else:
#         print("Enter right choice: ")
#         continue
#     if a==2:
#         sum=sum+1
#     elif a==3:
#         add=add+1
#
# if sum>add:
#     print("You won the game by winning ",sum," times")
# else:
#     print("You loose the game by loosing ",add," times")
#
#


# EG-3: