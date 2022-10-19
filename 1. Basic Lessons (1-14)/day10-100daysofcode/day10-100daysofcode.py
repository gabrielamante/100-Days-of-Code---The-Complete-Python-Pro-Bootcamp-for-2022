     # 10.1

def days_in_month(month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap() == True:
        month_days[1] += 1
    return month_days[month-1]

def is_leap():
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else: 
        return False 

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(month)
print(days)

    # 10.2 - Challenge - Calculator

from logo3 import logo

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1,n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        chosen_operation = input("Choose the operation above do you want to make: ")
        num2 = float(input("What's the next number? "))
        calculation_function = operations[chosen_operation]
        answer = calculation_function(num1,num2)

        print(f"{num1} {chosen_operation} {num2} = {answer}")

        option = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if option == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()