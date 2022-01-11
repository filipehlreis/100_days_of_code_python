"""
Calculator
"""

logo = """
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |      ██████  █████  ██       ██████ 
| |___|___|___| |___| |     ██      ██   ██ ██      ██      
| | 4 | 5 | 6 | | - | |     ██      ███████ ██      ██      
| |___|___|___| |___| |     ██      ██   ██ ██      ██      
| | 1 | 2 | 3 | | x | |      ██████ ██   ██ ███████  ██████ 
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

"""


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number? "))

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        should = input(f"Type 'y' to continue calculating with {answer}, or"
                       f" type 'n' to start a new calculation, or 'exit'"
                       f" to exit.: ")
        if should == 'y':
            num1 = answer
        elif should == 'exit':
            should_continue = False
        else:
            should_continue = False
            calculator()


calculator()
