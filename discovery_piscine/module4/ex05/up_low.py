#!/usr/bin/env python3

# ex05
# 2. Dar permissão de execução
# chmod +x up_low.py
#
# 3. Executar
# ./up_low.py


def up_low(text: str) -> str:
    return text.swapcase()


text: str = input("Enter a string: ")
print(up_low(text))