# Guess A Number Game

import random

computer_number = random.randint(1, 100)

while True:
    player_input = input("Guess the number (1-100): ")
    if not player_input.isdigit():
        print("The input is not a digit. Try again!")
        continue

    player_input = int(player_input)

    if player_input == computer_number:
        print("You guessed it!")
        break
    elif player_input < computer_number:
        print("Too low!")
    else:
        print("Too high!")
