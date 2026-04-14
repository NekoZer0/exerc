#!/usr/bin/env python3
#
# ex00
# 2. Dar permissão de execução
# chmod +x your_namebook.py
#
# 3. Executar # ./your_namebook.py 

# Método que recebe um dicionário e devolve lista de nomes completos
def array_of_names(persons: dict) -> list:
    result = []

    for first_name, last_name in persons.items():
        # capitaliza primeira letra de cada parte do nome
        full_name = first_name.capitalize() + " " + last_name.capitalize()
        result.append(full_name)

    return result


# Dados de teste
persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

# Execução
print(array_of_names(persons))