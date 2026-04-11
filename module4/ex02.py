#!/usr/bin/env python3

# ex02
# 2. Dar permissão de execução
# chmod +x calculator.py
#
# 3. Executar
# ./calculator.py


def calculator():

    try:
        first_number: float = float(input("Give me the first number: "))
        second_number: float = float(input("Give me the second number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number")
        return

    if second_number == 0:
        print("Error: Division by zero is not allowed.")
        return
    elif first_number.is_integer() and second_number.is_integer():
        display_number1 = int(first_number)
        display_number2 = int(second_number)

    else:
        display_number1 = first_number
        display_number2 = second_number

    print("Thank you!")
    print(f"{display_number1} + {display_number2} = {display_number1 + display_number2}")
    print(f"{display_number1} - {display_number2} = {display_number1 - display_number2}")
    print(f"{display_number1} / {display_number2} = {int(display_number1 / display_number2)if(display_number1 / display_number2).is_integer() else (display_number1/display_number2)}")
    print(f"{display_number1} * {display_number2} = {display_number1 * display_number2}")


calculator()
