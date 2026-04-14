#!/usr/bin/env python3

# ex00
# 2. Dar permissão de execução
# chmod +x upcase_it.py
#
# 3. Executar
# ./upcase_it.py


def upcase_it(text: str) -> str:
    return text.upper()


text: str = input("Give me a word: ")
print(upcase_it(text))