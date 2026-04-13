#!/usr/bin/env python3
#
# ex03
# 2. Dar permissão de execução
# chmod +x  append_it.py
#
#  3. Executar # append_it.py "Hello" "Hello " "zD"

import sys


def append_it() -> None:
    args = sys.argv[1:]

    # Se não houver parâmetros
    if len(args) == 0:
        print("none")
        return

    for arg in args:
        # O método find("ism") procura a substring "ism" dentro da string
        # e retorna:
        # - o índice (posição) onde começa "ism"
        # - ou -1 se não encontrar
        #
        # Exemplo:
        # "egoism".find("ism") → 3
        # "human".find("ism") → -1
        #
        # Aqui queremos saber se "ism" está no FINAL da palavra.
        # Para isso, comparamos com len(arg) - 3:
        # - "ism" tem 3 letras
        # - se começar exatamente em len(arg) - 3 → está no final
        #
        # Exemplo:
        # "egoism"
        # len = 6 → 6 - 3 = 3
        # find("ism") = 3 → está no final → NÃO imprime
        #
        # Se for diferente → não está no final → adiciona "ism"

        if arg.find("ism") != len(arg) - 3:
            print(arg + "ism")


append_it()
