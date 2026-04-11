#!/usr/bin/env python3

# ex03
# 2. Dar permissão de execução
# chmod +x advanced_mult.py
#
# 3. Executar
# ./advanced_mult.py

def show_multiplication_tables():
    table_number = 0  # controla qual tabela será exibida (de 0 até 10)

    while table_number <= 10:
        multiplier = 0  # controla os números dentro da tabela (de 0 até 10)

        # imprime o título da tabela
        print(f"Table of {table_number}:", end=" ")

        while multiplier <= 10:
            result = table_number * multiplier  # calcula a multiplicação
            print(result, end=" ")  # imprime o resultado na mesma linha

            multiplier += 1  # incrementa o multiplicador

        print()  # quebra de linha após terminar uma tabela

        table_number += 1  # passa para a próxima tabela


show_multiplication_tables()
