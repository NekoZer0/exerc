#!/usr/bin/env python3

# ex02
# 2. Dar permissão de execução
# chmod +x play_with_arrays.py
#
# 3. Executar
# ./play_with_arrays.py


def list_array(original_array: list):

    new_array = []

    for num in original_array:
        if num>5:
            new_array.append(num + 2)

    print(f"{original_array}")
    print(f"{new_array}")


list_array([2, 8, 9, 48, 8, 22, -12, 2])