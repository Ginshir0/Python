from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

options = Menu()
power_on = True
machine = CoffeeMaker()
funds = MoneyMachine()

while power_on:
    userInput = input("What would you like? (espresso/latte/cappuccino/):").lower()

    if userInput == "off":
        exit()
    if userInput == "report":
        machine.report()
        funds.report()
    else:
        if machine.is_resource_sufficient(options.find_drink(userInput)):
            item = options.find_drink(userInput)
            if funds.make_payment(item.cost):
                machine.make_coffee(options.find_drink(userInput))

