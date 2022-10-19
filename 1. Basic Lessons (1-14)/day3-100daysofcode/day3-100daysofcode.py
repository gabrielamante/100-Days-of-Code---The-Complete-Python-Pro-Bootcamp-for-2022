    #3.1

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

    #3.2

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = (weight / (height ** 2))
bmi_final = round(bmi)

if bmi_final < 18.5:
    print(f"Your BMI is {bmi_final}, you are underweight.")
elif bmi_final < 25:
    print(f"Your BMI is {bmi_final}, you have a normal weight.")
elif bmi_final < 30:
    print(f"Your BMI is {bmi_final}, you are slightly overweight.")
elif bmi_final < 35:
    print(f"Your BMI is {bmi_final}, you are obese.")
else:
    print(f"Your BMI is {bmi_final}, you are clinically obese.")

    #3.3

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is a Leap Year!")
        else:print("This is NOT a Leap Year!")
    else:print("This is a Leap Year!")
else: print("This is NOT a Leap Year!")

    #3.4

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
else:
    bill += 0

if extra_cheese == "Y":
    bill += 1
else:
    bill += 0

print(f"Your final bill is: ${bill}")

    #3.5 - CHALLENGE - SOLUTION 1

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

digit1 = name1.lower().count("t") + name1.lower().count("r") + name1.lower().count("u") + name1.lower().count("e") + name2.lower().count("t") + name2.lower().count("r") + name2.lower().count("u") + name2.lower().count("e")

digit2 = name1.lower().count("l") + name1.lower().count("o") + name1.lower().count("v") + name1.lower().count("e") + name2.lower().count("l") + name2.lower().count("o") + name2.lower().count("v") + name2.lower().count("e")

love_score_str = (str(digit1) + str(digit2))
love_score = int(love_score_str)

if love_score < 10 and love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

    #3.5 - CHALLENGE - SOLUTION 2

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combined_names = (name1 + name2).lower()

true_score = 0
love_score = 0

for letter in set("true"):
  true_score += combined_names.count(letter)
for letter in set("love"):
  love_score += combined_names.count(letter)

total_score = int(str(true_score) + str(love_score))

if total_score < 10 or total_score > 90:
  print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score >= 40 and total_score <= 50:
  print(f"Your score is {total_score}, you are alright together.")
else:
  print(f"Your score is {total_score}")

    #3.6 CHALLENGE 2

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

path1 = input("You're at a crossroad, where do you want to go? Type 'l' for left or 'r' for right: ").lower()
if path1 == 'l':
    path2 = input("You've come to and lake. There is an Island in the middle of the lake. Type 'w' to wait for a boat ou 's' to swim across: ")
    if path2 == 'w':
        path3 = input("You've found 3 doors with 3 different colours: Red, Blue and Yellow.Which one do you want to open? Type 'r' for the red one, 'b' for the blue one or 'y' for the yellow one: ")
        if path3 == 'y':
            print("You found the treasure!!")
            print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
        elif path3 == 'r':
            print("You were burned by the fire. Game Over.")
        elif path3 == 'b':
            print("You have been eaten by the Golems. Game Over.")
        else:
            print("Game Over.")
    else:
        print("You found Megalodon. Super Game Over.")
else:
    print("You have been hit by a airplane. Game Over.")