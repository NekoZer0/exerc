#!/usr/bin/env python3
#
# ex00
# 2. Dar permissão de execução
# chmod +x parameter_matching.py
#
#  3. Executar # parameter_matching.py "Hello"

import sys


def parameter_matching() -> None:
    args = sys.argv[1:]

    # Verifica se existe exatamente 1 argumento
    if len(args) != 1:
        print("none")
        return

    expected = args[0]

    # Pergunta ao utilizador
    user_input = input("What was the parameter? ")

    # Compara
    if user_input == expected:
        print("Good job!")
    else:
        print("Nope, sorry...")


parameter_matching()