# TODO: Choosing a random number between 1 and 100..
# TODO: Function to set difficulty
# TODO: Let the user guess a number
# TODO: Function to check users guess against actual answer
# TODO: Track the number of turns and reduce by 1 if they get it wrong
# TODO: Repeat the guessing functionality if they get it wrong.

import random
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard':")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too High 📈")
        return turns - 1
    elif guess < answer:
        print("Too Low 📉")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer} 🥳")
        return None


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            print(f"The answer is {answer}")
            return
        elif guess != answer:
            print("Guess again")

game()