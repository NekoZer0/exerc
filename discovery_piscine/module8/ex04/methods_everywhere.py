#!/usr/bin/env python3
#
# ex04
# 2. Dar permissão de execução
# chmod +x    methods_everywhere.py
#
#  3. Executar #   ./methods_everywhere.py 'lol' 'physically' 'backpack' | cat -e


import sys


class StringProcessor:
    # Método shrink: pega apenas os primeiros 8 caracteres (slicing)
    def shrink(self, text: str) -> str:
        return text[:8]

    # Método enlarge: adiciona 'Z' até completar 8 caracteres
    def enlarge(self, text: str) -> str:
        while len(text) < 8:
            text = text + "Z"
        return text


class App:
    def execute(self) -> None:
        args = sys.argv[1:]

        # Se não houver parâmetros
        if len(args) == 0:
            print("none")
            return

        processor = StringProcessor()

        for arg in args:
            if len(arg) > 8:
                print(processor.shrink(arg))
            elif len(arg) < 8:
                print(processor.enlarge(arg))
            else:
                print(arg)


App().execute()