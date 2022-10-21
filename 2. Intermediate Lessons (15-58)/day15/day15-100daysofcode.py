    # Coffee Maker

from data import MENU, resources, emoji_coffee


def _is_resource_sufficient(order_ingredients):
    """Returns if the machine have ingredients enough to prepare the order."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def _calculate_payment():
    """Calculates the ommount of money the client deposited in coins."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def _check_transaction(payment, order_price):
    """Return True when the payment is accepted or False if money is insufficient."""
    if payment > order_price:
        change = round(payment-order_price, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += order_price
        return True
    elif payment < order_price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        return True


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= drink[item]
    print(f"Here is your {drink_name} ☕")



profit = 0
is_on = True

while is_on:
    order = input("What would you like? An Espresso, a Latte or a Cappuccino?: ").lower()
    if order == 'off':
        is_on = False
    elif order == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}")
    else:
        drink = MENU[order]
        if _is_resource_sufficient(drink["ingredients"]):
            payment = _calculate_payment()
            if _check_transaction(payment=payment, order_price=drink["cost"]):
                make_coffee(drink_name=order,order_ingredients=drink["ingredients"])