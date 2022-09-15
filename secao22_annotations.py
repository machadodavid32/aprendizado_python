# import math

"""
def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio


print(circunferencia.__annotations__)

# resposta: {'raio': <class 'float'>, 'return': <class 'float'>}
# O annotations informa os tipos da função

nome: str = "David"
peso: float = 82.4
ativo: bool = True

print(nome)
print(peso)
print(ativo)
print(__annotations__)

# Resposta: David
# 82.4
# True
# {'nome': <class 'str'>, 'peso': <class 'float'>, 'ativo': <class 'bool'>}
"""


class Pessoa:
    def __int__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome: str = nome
        self.__idade: int = idade
        self.__peso: float = peso

    def andar(self) -> str:
        return f'{self.__nome} está andando'


p = Pessoa(nome='David', idade=42, peso=82.7)

print(p.__dict__)