from coffee_machine.menu import Menu
from coffee_machine.coffee_maker import CoffeeMaker
from coffee_machine.money_machine import MoneyMachine

from replit import clear

clear()

menu_machine = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

is_on = True
while is_on:
    choice = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == 'off':
        is_on = False
        print("Turning coffee machine off.")
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu_machine.find_drink(choice)
        if drink:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
