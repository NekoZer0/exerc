#!/usr/bin/env python3

# ex04
# 2. Dar permissão de execução
# chmod +x scan_it.py
#
# 3. Executar
# ./scan_it.py  "Python" "piscine" "hello"

import sys
import re


def scan_it() -> None:
    args = sys.argv[1:]

    # Verifica se existem exatamente 2 parâmetros
    if len(args) != 2:
        print("none\n")
        return

    keyword = args[0]
    text = args[1]

    # Escapa caracteres especiais da keyword (importante!)
    pattern = re.escape(keyword)

    # Encontra todas as ocorrências
    matches = re.findall(pattern, text)

    # Verifica resultado
    if len(matches) == 0:
        print("none\n")
    else:
        print(len(matches))


scan_it()