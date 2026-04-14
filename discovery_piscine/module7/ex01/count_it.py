#!/usr/bin/env python3
#
# ex01
# 2. Dar permissão de execução
# chmod +x count_it.py
#
#  3. Executar # count_it.py "Hello" "Hello " "zD"

import sys


def count_it() -> None:
    args = sys.argv[1:]

    # Se não houver parâmetros
    if len(args) == 0:
        print("none")
        return

    # Número total de parâmetros
    print(f"parameters: {len(args)}")

    # Para cada parâmetro, mostra o valor e o tamanho
    for arg in args:
        print(f"{arg}: {len(arg)}")


count_it()