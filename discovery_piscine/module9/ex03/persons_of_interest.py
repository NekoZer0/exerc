#!/usr/bin/env python3
#
# ex02
# 2. Dar permissão de execução
# chmod +x persons_of_interest.py
#
# 3. Executar # ./persons_of_interest.py

#!/usr/bin/env python3


class HistoricalFigures:
    # Método que ordena e imprime pessoas por data de nascimento
    def famous_births(self, people: dict) -> None:
        
        # sorted() ordena pelos valores do dicionário (date_of_birth)
        # items() devolve (key, value)
        sorted_people = sorted(
            people.items(),
            key=lambda item: item[1]["date_of_birth"]
        )

        # Itera pelos elementos ordenados
        for _, data in sorted_people:
            print(f"{data['name']} is a great scientist born in {data['date_of_birth']}.")


# Dados de teste
women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

# Execução
history = HistoricalFigures()
history.famous_births(women_scientists)