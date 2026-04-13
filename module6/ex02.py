#!/usr/bin/env python3

# ex02
# 2. Dar permissão de execução
# chmod +x downcase_it.py

#
# 3. Executar
# ./downcase_it.py  "FIREFLY"


import sys

def parameters() -> str:

    args = sys.argv[1:]

    if len(args) != 1:
        return f"{None}\n"

    return f"{args[0].lower()}\n"
    

print(parameters())
