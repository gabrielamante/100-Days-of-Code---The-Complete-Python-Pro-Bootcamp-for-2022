    # Challenge - HANGMAN

import random
from words import word_list
from stages import stages
from logo import logo

end_of_game = False
chosen_word = random.choice(word_list)
lenght = len(chosen_word)
lives = 6
print(logo)

display = []
for letter in chosen_word:
    display.append("_")
print(display)

while not end_of_game:
    
    print(f"You have {lives} lives")
    
    guess = str(input("Guess a letter: ")).lower()
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(lenght):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed wrong, {guess} isn't in the word. You lost a life!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lost.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You won!")
    
    print(stages[lives])