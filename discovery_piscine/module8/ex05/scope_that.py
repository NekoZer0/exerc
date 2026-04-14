#!/usr/bin/env python3
#
# ex05
# 2. Dar permissão de execução
# chmod +x     scope_that.py
#
#  3. Executar #   ./scope_that.py | cat-e


class ScopeDemo:
    # Método que adiciona 1 e RETORNA o novo valor
    def add_one(self, value):
        return value + 1


class App:
    def execute(self) -> None:
        number = 5

        # mostra valor inicial
        print(number)

        demo = ScopeDemo()

        # atualizar a variável com o valor retornado
        number = demo.add_one(number)

        print(number)  # mostra o valor atualizado
        print(number-1)  # mostra o valor original


App().execute()
