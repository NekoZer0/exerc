#!/usr/bin/env python3

# ex03
# 2. Dar permissão de execução
# chmod +x aff_rev_params.py
#
# 3. Executar
# ./aff_rev_params.py  "Python" "piscine" "hello"


import sys


def aff_rev_params():

    args = sys.argv[1:]

    if len(args) >= 2:
        for arg in reversed(args):
            print(f"{arg}")
        print("")
    else:
        print(f"{None}\n")


aff_rev_params()
