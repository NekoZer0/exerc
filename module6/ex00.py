#!/usr/bin/env python3

# ex00
# 2. Dar permissão de execução
# chmod +x aff_first_param.py
#
# 3. Executar
# ./aff_first_param.py  "Code Ninja" "Numeric" "42" 



import sys

# Permite acesso a funcionalidades do sistema, como:
# - argumentos da linha de comando (sys.argv)
# - saída do programa
# - informações do interpretador

def parameters()-> str | None:

    args = sys.argv[1:]
    
    if len(args) > 0:
        return f"{args[0]}"
    
    return None

print(parameters())
 