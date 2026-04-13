#!/usr/bin/env python3
#
# ex04
# 2. Dar permissão de execução
# chmod +x  free_range.py
#
#  3. Executar # free_range.py 1 10

import sys


def free_range() -> None:
    args = sys.argv[1:]

    # Verifica se existem exatamente 2 parâmetros
    if len(args) != 2:
        print("none")
        return

    try:
        start = int(args[0])
        end = int(args[1])
    except ValueError:
        # Caso não sejam números
        print("none")
        return

    # O primeiro número deve ser estritamente menor que o segundo
    if start >= end:
        print("none")
        return

    # Cria a lista com range (incluindo o último número)
    numbers = list(range(start, end + 1))

    print(numbers)


free_range()
