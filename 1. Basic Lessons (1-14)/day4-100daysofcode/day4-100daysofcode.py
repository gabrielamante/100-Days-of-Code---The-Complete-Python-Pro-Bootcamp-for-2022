randon_int = random.randint(1,10)
print(randon_int)

#List functions: https://docs.python.org/3/tutorial/datastructures.html

# print(list[x][y]) - printa o elemento y da lista x

    #4.1
import random

coin_flip = random.randint(0,1)
print(coin_flip)

if coin_flip == 1:
    print("Heads")
else:
    print("Tails")

    #4.2
import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
tamanho = len(names)

index = random.randint(0,tamanho)

print(f"{names[index]} is going to buy the meal today!")

    #4.3

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")
position1 = int(position[0])-1
position2 = int(position[1])-1

map[position2][position1] = "X"

print(f"{row1}\n{row2}\n{row3}")

    #4.4 - CHALLENGE

import random

rock = ''' rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = ''' paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = ''' scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type '0' for Rock, '1' for Paper or '2' for Scissors: "))
pc_choice = random.randint(0,2)

print(rps[user_choice])
print("Computer chose:")
print(rps[pc_choice])

if user_choice == 0 and pc_choice == 2:
    print("You won!")
elif user_choice == 2 and pc_choice == 0:
    print("You lost.")
elif pc_choice > user_choice:
    print("You lost.")
elif user_choice > pc_choice:
    print("You won.")
elif user_choice == pc_choice:
    print("Draw.")