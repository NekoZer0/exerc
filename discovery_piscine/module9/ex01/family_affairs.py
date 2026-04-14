#!/usr/bin/env python3
#
# ex01
# 2. Dar permissão de execução
# chmod +x family_affairs.py
#
# 3. Executar # ./family_affairs.py


class FamilyAffairs:
    # Método que encontra pessoas com cabelo ruivo
    def find_the_redheads(self, family: dict) -> list:
        
        # filter() percorre o dicionário (pelas chaves)
        # e mantém apenas os nomes cuja cor é "red"
        redheads = filter(
            lambda name: family[name] == "red",
            family.keys()
        )

        # converte o resultado do filter em lista
        return list(redheads)


# Dados de teste
dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

# Execução
family = FamilyAffairs()
print(family.find_the_redheads(dupont_family))