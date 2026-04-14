#!/usr/bin/env python3

# ex00
# 2. Dar permissão de execução
# chmod +x to25.py
#
# 3. Executar
# ./to25.py

def number_print():

    try:
        number: int = int(input("Enter a number less than 25\n"))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    if number > 25:
        print("ERROR\n")
    else:
       while number <= 25:
            print(f"Inside the loop, my variable is {number}")
            number += 1
number_print()