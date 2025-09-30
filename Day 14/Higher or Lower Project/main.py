import random
from art import logo, vs
from game_data import data
print(logo)

score = 0
game_continue = True

def question_formation(player):
    return f"{player["name"]}, a {player["description"]}, from {player["country"]}."

def check_answer(user_guess, player_a, player_b):
    if player_a["follower_count"] > player_b["follower_count"]:
        return user_guess == "a"
    else:
        return user_guess == "b"


while game_continue:
    player_a = random.choice(data)
    player_b = random.choice(data)

    if player_a == player_b:
        player_b = random.choice(data)
    else:
        print(f"Compare A: {question_formation(player_a)}")
        print(vs)
        print(f"Against B: {question_formation(player_b)}")

    guess = input("Who has more followers? Type 'A' or 'B':").lower()

    correct_answer = check_answer(guess,player_a,player_b)

    if correct_answer:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_continue = False