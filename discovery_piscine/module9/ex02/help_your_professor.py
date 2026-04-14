#!/usr/bin/env python3
#
# ex02
# 2. Dar permissão de execução
# chmod +x help_your_professor.py
#
# 3. Executar # ./help_your_professor.py

class GradeBook:
    # Método que calcula a média da turma
    def average(self, students: dict) -> float:
        total = sum(students.values()) #pega apenas os valores do dicionário: e soma
        count = len(students) # pega número de alunos no dicionario

        return total / count


# Dados de teste
class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

# Execução
gradebook = GradeBook()

print(f"Average for class 3B: {gradebook.average(class_3B)}.")
print(f"Average for class 3C: {gradebook.average(class_3C)}.")