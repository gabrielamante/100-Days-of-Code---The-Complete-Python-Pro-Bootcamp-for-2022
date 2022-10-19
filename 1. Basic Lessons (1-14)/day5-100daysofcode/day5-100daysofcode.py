     #5.1
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

altura_total = 0
tamanho_lista = 0

for i in student_heights:
    altura_total += i
    tamanho_lista += 1

media_altura = round(altura_total/tamanho_lista)
print(media_altura)

    #5.2

student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

maxscore = 0

for score in student_scores:
    if score > maxscore:
        maxscore = score

print(f"The highest score in the class is: {maxscore}")

    #5.3

total = 0
for n in range(0,102,2):
    total += n
print(total)

    #5.4

for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

    #5.5 - DESAFIO - EASIER

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword generator!")
l = int(input("How many letters would you like in your password?\n"))
s = int(input("How many symbols would you like?\n"))
n = int(input("How many numbers would you like?\n"))

password = ""

for i in range(1,l+1):
    password += random.choice(letters)
for j in range(1,n+1):
    password += random.choice(numbers)
for k in range(1,s+1):
    password += random.choice(symbols)

print(password)

    #5.6 - DESAFIO - HARDER

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword generator!")
l = int(input("How many letters would you like in your password?\n"))
n = int(input("How many numbers would you like?\n"))
s = int(input("How many symbols would you like?\n"))

password_list = []

for i in range(1,l+1):
    password_list.append(random.choice(letters))
for j in range(1,n+1):
    password_list.append(random.choice(numbers))
for k in range(1,s+1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")