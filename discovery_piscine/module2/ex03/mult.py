#!/usr/bin/env python3

# ex03
# 2. Dar permissão de execução
# chmod +x mult.py
#
# 3. Executar
# ./mult.py

def mult():

    try:
        number1: float = float(input("Enter the first number: "))
        number2: float = float(input("Enter the second number: "))

    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    if number1.is_integer() and number2.is_integer():
        display_number1 = int(number1)
        display_number2 = int(number2)
    else:
        display_number1 = number1
        display_number2 = number2

    resulttado = display_number1 * display_number2

    if resulttado > 0:
        print(
            f"{display_number1} x {display_number2} = {resulttado}\nThis result is positive.")
    elif resulttado < 0:
        print(
            f"{display_number1} x {display_number2} = {resulttado}\nThis result is negative.")
    else:
        print(
            f"{display_number1} x {display_number2} = {resulttado}\nThis result is zero")

mult()