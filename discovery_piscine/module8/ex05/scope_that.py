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
        #value=value+1
        return value + 1


class App:
    def execute(self) -> None:
        number = 5
        value_numeber= number

        # mostra valor inicial
        print(number)

        demo = ScopeDemo()

        # atualizar a variável com o valor retornado
        #demo.add_one(number)
        number = demo.add_one(number)

        print(number)
        print (value_numeber)
    

App().execute()