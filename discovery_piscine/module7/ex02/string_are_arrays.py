#!/usr/bin/env python3
#
# ex02
# 2. Dar permissão de execução
# chmod +x  string_are_arrays.py
#
#  3. Executar # string_are_arrays.py "Hello" "Hello " "zD"



import sys


def string_are_arrays() -> None:
    args = sys.argv[1:]

    if len(args) != 1:
        print("none")
        return

    text = args[0]

    count = 0

    # Percorre a string como um array
    for char in text:
        if char == 'z':
            count += 1

    if count == 0:
        print("none")
    else:
        print('z' * count)


string_are_arrays()