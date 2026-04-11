#!/usr/bin/env python3

# ex03
# 2. Dar permissão de execução
# chmod +x float.py
#
# 3. Executar
# ./float.py


def This_number_is():

    try:
        number: float = float(input("Give me a number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number")
        return

    if number.is_integer() :
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
    

This_number_is()