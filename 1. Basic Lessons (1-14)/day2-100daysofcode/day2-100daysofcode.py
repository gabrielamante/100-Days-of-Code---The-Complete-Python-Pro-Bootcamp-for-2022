    #2.1

two_digit_number = input("Type a two digit number: ")

print(int(two_digit_number[0]) + int(two_digit_number[1]))

    #2.2

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = (weight / (height ** 2))
bmi_as_int = int(bmi)
print(bmi_as_int)

    #2.3

idade = int(input("What is your current age?\n"))

idade_meses = (90 - idade) * 12
idade_semanas = (90 - idade) * 52
idade_dias = (90 - idade) * 365

print(f"You have {idade_dias} days, {idade_semanas} weeks and {idade_meses} months left.")

    #2.4 - CHALLENGE