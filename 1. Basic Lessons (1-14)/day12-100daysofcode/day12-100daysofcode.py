#Number Guessing Game Objectives:

from logo5 import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_guess(guess, chosen_number, turns):
    if guess > chosen_number:
        print("Too high.")
        return turns - 1
    elif guess < chosen_number:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The chosen number was {chosen_number}")


def set_difficulty():
    level = input("\nChoose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    print("\nWelcome to the Number Guessing Game!\nI'm thinking about a number between 1 and 100.")

    chosen_number = random.randint(1,100)
    turns = set_difficulty()

    guess = 0
    while guess != chosen_number:
        print(f"\nYou have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_guess(guess,chosen_number,turns)
        if turns == 0:
            print(f"You ran out of guesses. You lost. The number was {chosen_number}.")
            return

game()