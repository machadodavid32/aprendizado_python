"""def cumprimentar(nome: str) -> str:
    "Acima é uma função com parametro 'nome' que é do tipo string e retorna um valor do tipo string"
    return f'Olá, {nome}'

print(cumprimentar('David'))

# Acima estamos definindo que o parametro seja uma string e o retorno também seja uma string...
# ... isso é o typinh hinting
"""

"""
def cabecalho(texto, alinhamento=True):
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


print(cabecalho('geek university'))

# Resposta:
# Geek University
# ---------------
# Nesta resposta, o primeiro return entrou. O title() serviu para deixar as primeiras letras em maíusculo...
# ... e a parte \n{'-' * len(texto)} serviu para multiplicar os pontilhados x geek university e foi pra linha...
# ... de baixo.

print(cabecalho('geek university', alinhamento=False))
# Resposta: ################ Geek University #################

# Na resposta acima, colocando o alinhamento como False, acionou o segundo return f" {texto.title()} ".center(50, '#')
# ...Neste caso, o comando .center alinhou o 'Geek University' e o número 50 é o numero de # que tem aos lados.
"""

# Abaixo vamos refatorar a função para o typinh hinting


def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


print(cabecalho('geek university'))

print(cabecalho('geek university', alinhamento=False))

# Resposta: Geek University
# ---------------
# ################ Geek University #################


# A vantagem de utilizar o typing hinting é para evitar erros na produção de programas e aplicativos