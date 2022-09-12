"""
Doctests - teste que vai dentro da documentação da sua função.

Para rodar um teste do doctest:

python -m doctest -v nome_do_modulo.py


"""

def soma(a, b):
    """ Soma os números a e b

    >>> soma(1, 2)
    3
    """
    return a + b

print(soma(3, 4))
# Resposta: 7

# para visualizar o teste, basta essa linha de comando: 
# python -m doctest -v doctests.py(esse ultimo é o nome do arquivo)
# no terminal python