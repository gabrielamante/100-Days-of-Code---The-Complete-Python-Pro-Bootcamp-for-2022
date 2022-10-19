    # BLACKJACK

import random
from logo4 import logo

def deal_card():
    """ Returns a random card from the deck. """
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """ Calculates the score from a list of cards and returns the score. """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, house_score):
    """ Compare the scores of the house and the user to check who won. """
    if user_score == house_score:
        return "Draw 🙃"
    elif house_score == 0:
        return "You lost. The house has a Blackjack 😱"
    elif user_score == 0:
        return "You won with a Blackjack! 😎"
    elif user_score > 21:
        return "You lost. Went over 21 😭"
    elif house_score > 21:
        return "You won! House went over 21 😁"
    elif user_score > house_score:
        return "You won! 😃"
    else:
        return "You lost. 😤"

def play_game():

    print(logo)
    user_cards = []
    house_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        house_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        house_score = calculate_score(house_cards)
        print(f"Your hand: {user_cards}, current score: {user_score}")
        print(f"Computer's hand: {house_cards[0]}")

        if user_score == 0 or house_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card or type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while house_score != 0 and house_score < 17:
        house_cards.append(deal_card())
        house_score = calculate_score(house_cards)
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {house_cards}, final score: {house_score}")

    comparision = compare(user_score=user_score, house_score=house_score)
    print(comparision)

while input("\nDo you want to play another game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()