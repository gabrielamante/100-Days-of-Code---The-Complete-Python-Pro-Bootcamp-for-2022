from logo6 import logo
from instagram_data import data
import random

def check_answer(guess,followers_a,followers_b):
    """ Takes the guess and check if it's right comparing the number of followers of A and B"""
    if followers_a > followers_b:
        return guess == 'a'
    else:
        return guess == 'b'

print(logo)
score = 0
game_should_continue = True
b = data.index(random.choice(data))

# data index: [0]=name  [1]=follower_count(int)  [2]-description  [3]-country

while game_should_continue:

    a = b
    b = data.index(random.choice(data))
    if a == b:
        b = data.index(random.choice(data))
    
    followers_a = int(data[a]['follower_count'])
    followers_b = int(data[b]['follower_count'])

    print(f"Compare A: {data[a]['name']}, a {data[a]['description']} from {data[a]['country']}.")
    print("\nVS\n")
    print(f"Against B: {data[b]['name']}, a {data[b]['description']} from {data[b]['country']}.")

    guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()
    is_correct = check_answer(guess,followers_a,followers_b)

    if is_correct:
        score += 1
        print(f"That's correct! Current score is {score}.")
    else:
        game_should_continue = False
        print(f"You're wrong. Final score is {score}.")

# print(logo)