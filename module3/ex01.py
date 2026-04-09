#!/usr/bin/env python3

# ex01
# 2. Dar permissão de execução
# chmod +x multiplication_table.py
#
# 3. Executar
# ./multiplication_table.py

def multiplication_table():

    try:
        number: int = int(input("Enter a number\n"))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    for increment in range(0, 10):
        print(f"{increment} x {number} = {increment * number}")
        
multiplication_table()
