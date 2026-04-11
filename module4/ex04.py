#!/usr/bin/env python3

# ex04
# 2. Dar permissão de execução
# chmod +x round_up.py
#
# 3. Executar
# ./round_up.py


import math

def this_number_round_up() -> int:
    try:
        number: float = float(input("Give me a number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number")
        return 0
        
    return math.ceil(number)

print(this_number_round_up())