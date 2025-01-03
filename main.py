import art
import os
import platform

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def square(n1, n2):
    return n1 ** n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": square,
}

def calculation():
    print(art.logo)
    num1 = float(input("What is the first number?: "))
    is_accumulated = True
    while is_accumulated:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        result = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

        if choice == "y":
            num1 = result
        else:
            is_accumulated = False
            clear_screen()
            calculation()


calculation()