#!/usr/bin/env python3

# ex04
# 2. Dar permissão de execução
# chmod +x parameters.py
#
# 3. Executar
# ./parameters.py "this" "is" "crazy" "there's" "everywhere!"



import sys

# Permite acesso a funcionalidades do sistema, como:
# - argumentos da linha de comando (sys.argv)
# - saída do programa
# - informações do interpretador

def parameters():

    args = sys.argv[1:]
    # ↑ sys.argv é uma lista automática criada pelo Python com os argumentos da execução

    # Exemplo:
    # ./parameters.py a b c
    # sys.argv = ["./parameters.py", "a", "b", "c"]

    # sys.argv[0] -> nome do ficheiro/script
    # sys.argv[1:] -> todos os argumentos reais passados pelo utilizador

    # Entao nosso args = sys.argv[1:] vai conter apenas os argumentos reais, sem o nome do ficheiro
    # args = ["a", "b", "c"]

    print(f"Number of parameters: {len(args)}.")
     
parameters()
 