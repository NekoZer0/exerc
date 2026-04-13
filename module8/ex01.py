#!/usr/bin/env python3
#
# ex01
# 2. Dar permissão de execução
# chmod +x    upcase_it.py
#
#  3. Executar # upcase_it.py


class TextProcessor:
    # Método da classe
    def upcase_it(self, text: str) -> str:
        return text.upper()


# Criar objeto da classe
processor = TextProcessor()

# Chamar o método e testar
print(processor.upcase_it("hello"))
