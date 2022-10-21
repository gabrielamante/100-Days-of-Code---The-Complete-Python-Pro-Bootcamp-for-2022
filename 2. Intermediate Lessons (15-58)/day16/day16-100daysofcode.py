from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    menu_items = menu.get_items()
    order = input(f"What would you like? {menu_items}: ")
    if order == "off":
        is_on = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order_name=order)
        if coffee_maker.is_resource_sufficient(drink=drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)