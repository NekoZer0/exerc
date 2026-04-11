
#!/usr/bin/env python3

# ex01
# 2. Dar permissão de execução
# chmod +x isneg.py
#
# 3. Executar
# ./isneg.py


def this_number_is():
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

        if number > 0:
            print(f"{display_number}\nThis number is positive.")
        elif number < 0:
            print(f"{display_number}\nThis number is negative.")
        else:
            print(f"{display_number}\nThis number is both positive and negative.")
            break


this_number_is()
