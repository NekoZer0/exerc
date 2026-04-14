#!/usr/bin/env python3
#
# ex02
# 2. Dar permissão de execução
# chmod +x    downcase_it.py
#
#  3. Executar # ./downcase_it.py  "HELLO WORLD" "I understood Arrays well!"

import sys


class TextProcessor:
    # Método que converte para minúsculas
    def downcase_it(self, text: str) -> str:
        return text.lower()


class App:
    # Método de execução (sem usar main)
    def execute(self) -> None:
        args = sys.argv[1:]

        # Se não houver parâmetros
        if len(args) == 0:
            print("none")
            return

        processor = TextProcessor()

        # Aplicar método a cada argumento
        for arg in args:
            print(processor.downcase_it(arg))


# Execução do programa
App().execute()