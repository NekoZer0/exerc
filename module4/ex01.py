#!/usr/bin/env python3

# ex01
# 2. Dar permissão de execução
# chmod +x age.py
#
# 3. Executar
# ./age.py


def age():

    try:
        age_number: int = int(input("Please tell me your age: "))
    except ValueError:
        print("Invalid input: Age must be an integer")

    print(f"You are currently {age_number} years old.")
    print(f"In 10 years, you'll be {age_number + 10} years old.")
    print(f"In 20 years, you'll be {age_number + 20} years old.")
    print(f"In 30 years, you'll be {age_number + 30} years old.")


age()