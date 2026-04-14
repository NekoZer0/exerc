#!/usr/bin/env python3

# ex00
# 2. Dar permissão de execução
# chmod +x iszero.py
#
# 3. Executar
# ./iszero.py


def number_print():
    while True:
        try:
            number: float = float(input("Insert one number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if number.is_integer():
            display_number = int(number)
        else:
            display_number = number

        if number == 0:
            print(f"{display_number}\nThis number is equal to zero.")
            break

        print(f"{display_number}\nThis number is different from zero.")


number_print()
