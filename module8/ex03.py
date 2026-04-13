#!/usr/bin/env python3
#
# ex03
# 2. Dar permissão de execução
# chmod +x    greetings_for_all.py
#
#  3. Executar #  cat greetings_for_all.py | cat-e


class Greeter:
    # Método com parâmetro padrão
    def greetings(self, name="noble stranger") -> None:

        # Verifica se o argumento é uma string
        if not isinstance(name, str):
            print("Error! It was not a name.")
            return

        print(f"Hello, {name}.")


# Criar objeto da classe
greeter = Greeter()

# Testes pedidos no enunciado
greeter.greetings("Alexandra")
greeter.greetings("Wil")
greeter.greetings()
greeter.greetings(42)