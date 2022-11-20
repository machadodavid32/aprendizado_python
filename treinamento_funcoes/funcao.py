"""
def soma(n1, n2):
    print(n1 + n2)

soma(2, 3)


def sub(n1, n2):
    print(n1 - n2)

sub(5, 18)

def fale(fala, resposta):
    print(fala, resposta)

fale('oi', 'tudo bem')


def multiplicacao(a, b):
    print(a * b)


multiplicacao(2, 7)    


def soma_numeros(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total  


print(soma_numeros(3, 3))


def soma_todos_numeros(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total

print(soma_todos_numeros(2, 3))


def diz_ola():
    return 1981

print(f'Hoje é {diz_ola()}')





from random import random

def joga_moeda():
    joga = random()
    if joga >= 0.5:
        return "cara"
    if joga <= 0.5:
        print("coroa")

print(joga_moeda())




def eh_impar():
    numero = 7
    if numero %2 != 0:
        return True
    return False

print(eh_impar())        
"""

total = 0

def teste():
    global total
    total = total + 1
    if total >= 0:
        return "Deu certo"

print(teste())


def nome_completo(nome, sobrenome):
    return f'Seu nome é {nome} {sobrenome}'
    

print(nome_completo('David', 'Machado'))


