#!/usr/bin/env python3

# ex01
# 2. Dar permissão de execução
# chmod +x upcase_it.py

#
# 3. Executar
# ./upcase_it.py  "Code Ninja" "Numeric" "42"


import sys

def parameters() -> str:

    args = sys.argv[1:]

    if len(args) != 1:
        return f"{None}\n"

    return f"{args[0].upper()}"


print(parameters())
