from replit import clear

logo = """                   __  __          
                  / _|/ _|         
         ___ ___ | |_| |_ ___  ___ 
        / __/ _ \|  _|  _/ _ \/ _ \\
       | (_| (_) | | | ||  __/  __/
        \___\___/|_| |_| \___|\___|
        /~~~~~~~~~~~~~~~~~~~/|
       /              /######/ / |
      /              /______/ /  |
     ========================= /||
     |_______________________|/ ||
      |  \****/     \__,,__/    ||
      |===\**/       __,,__     ||
      |______________\====/%____||
      |   ___        /~~~~\ %  / |
     _|  |===|===   /      \%_/  |
    | |  |###|     |########| | /
    |____\###/______\######/__|/
    ~~~~~~~~~~~~~~~~~~~~~~~~~~ 
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 100,
}


def check_resources(client_option, resources):
    """Check resources based in client option drink and returns 'TRUE' if 
    is OK or 'FALSE' if it's missing something."""
    client_drink = MENU[client_option]

    missing_ingredients_flag = False
    missing_ingredients_string = "Sorry, that's not enough "
    missing_ingredients = []

    for ingredient in client_drink["ingredients"]:
        if client_drink["ingredients"][ingredient] >= resources[ingredient]:
            missing_ingredients_flag = True
            missing_ingredients.append(ingredient)

    if missing_ingredients_flag:
        missing_ingredients_string += ", ".join(missing_ingredients) + ".\n"
        print(missing_ingredients_string)
        return False
    return True


def print_report(resources):
    print(
        f"\nReport:"
        f"\n  - Water :  {resources['water']:4} ml"
        f"\n  - Milk  :  {resources['milk']:4} ml"
        f"\n  - Coffee:  {resources['coffee']:4} g"
        f"\n  - Money :  ${resources['money']:4.2f}\n"
    )


def insert_coins():
    """Ask the user to insert coins and returns the sum of money inserted."""
    print(
        "\nPlease insert coins.\n"
        "quarters = $0.25, dimes = $0.10, "
        "nickles = $0.05, pennies = $0.01\n"
    )
    coin_quarters = int(input("How many quarters? "))
    coin_dimes = int(input("How many dimes?    "))
    coin_nickles = int(input("How many nickles?  "))
    coin_pennies = int(input("How many pennies?  "))

    money_inserted = (coin_quarters*0.25 + coin_dimes*0.10 +
                      coin_nickles*0.05 + coin_pennies*0.01)

    print(f"\nYou inserted ${money_inserted:.2f}.\n")
    return money_inserted


def check_transaction_successful(drink_cost_value, money_inserted):
    """Returns 'TRUE' if money inserted is greater or equal than drink cost,
    else returns 'FALSE'."""
    if drink_cost_value <= money_inserted:
        return True
    return False


def drink_cost(client_option):
    """Return drink cost value."""
    drink_cost_value = MENU[client_option]["cost"]
    return drink_cost_value


def check_transaction_change(drink_cost_value, money_inserted):
    """Returns 'TRUE' if money inserted is greater than drink cost and
    need change, else returns 'FALSE'"""
    if money_inserted > drink_cost_value:
        return True
    return False


def transaction_change(drink_cost_value, money_inserted):
    """Returns value of change"""
    return money_inserted - drink_cost_value


def make_coffe(client_option, resources_f):
    """Returns deducted resources for the coffee choosed."""
    client_drink = MENU[client_option]
    for ingredient in client_drink["ingredients"]:
        resources[ingredient] = resources[ingredient] - \
            client_drink["ingredients"][ingredient]
    return resources_f


def coffee_machine(resources):
    should_coffe_machine_continue = True
    print(logo)

    while should_coffe_machine_continue:
        # TODO: 1. Prompt user by asking "What would you like?
        client_choose = input(
            "What would you like? (espresso/latte/cappuccino): ").lower()

        if client_choose == 'off':
            # TODO: 2. Turn off the Coffee Machine by entering “off”.
            print("Turning the coffee machine off.")
            should_coffe_machine_continue = False
            return

        elif client_choose == 'report':
            # TODO: 3. Print report.
            print_report(resources)

        elif client_choose in MENU:
            # TODO: 4. Check resources sufficient?
            if check_resources(client_choose, resources):
                drink_cost_value = drink_cost(client_choose)
                print(f"Your drink costs ${drink_cost_value:.2f}.")

                # TODO: 5. Process coins.
                money_inserted = insert_coins()

                # TODO: 6. Check transaction successful?
                if check_transaction_successful(drink_cost_value,
                                                money_inserted):
                    if check_transaction_change(drink_cost_value,
                                                money_inserted):
                        money_change = transaction_change(
                            drink_cost_value, money_inserted)
                        print(
                            f"Here is ${money_change:.2f} "
                            f"dollars in change.\n")

                    resources["money"] = resources["money"] + drink_cost_value

                    # TODO: 7. Make Coffee.
                    resources = make_coffe(client_choose, resources)

                    print(
                        f"Here is your {client_choose.capitalize()}. Enjoy!\n")

                else:
                    print("Sorry that's not enough money. Money refunded.")


clear()
coffee_machine(resources)
