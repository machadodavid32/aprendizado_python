"""
nomes: list = ['geek', 'university']

versoes: tuple = (3, 4, 7,)

opcoes: dict = {'ar': True, 'banco_couro': True}

valores: set = {3, 4, 5, 6}

print(nomes, versoes, opcoes, valores)

print(__annotations__)

# Respostas: ['geek', 'university'] (3, 4, 7) {'ar': True, 'banco_couro': True} {3, 4, 5, 6}
# {'nomes': <class 'list'>, 'versoes': <class 'tuple'>, 'opcoes': <class 'dict'>, 'valores': <class 'set'>}

# Acima nós conseguimos definir qual o tipo de dado. Mas e dentro dos dados? Ver abaixo:


nomes: list[str] = ["david"]

"""

import random
NAIPES = '♠ ♡ ♢ ♣'.split()  # icone das cartas em https://www.alt-codes.net/suit-cards.php
CARTAS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()  # lembrar que o split serve para separar as strings


def criar_baralho(aleatorio=False):
    """Cria um baralho com 52 cartas"""
    baralho = [(n, c) for c in CARTAS for n in NAIPES]
    if aleatorio:
        random.shuffle(baralho)
    return baralho


def distribuir_cartas(baralho):
    """Gerencia a mão de cartas de acordo com o baralho gerado"""
    return baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4]


def jogar():
    """Inicia um jogo de cartas para quatro jogadores"""
    cartas = criar_baralho(aleatorio=True)
    jogadores = 'P1 P2 P3 P4'.split()
    maos = {j: m for j, m in zip(jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        carta = ' '.join(f"{j}{c}" for (j, c) in cartas)
        print(f'{jogador}: {carta}')


if __name__ == "__main__":
    jogar()

    
