"""
O operador Walrus permite fazer a atribuição e retorna de valor em uma unica expressão

variavel := expressao

"""

nome = 'geek university'
print(nome)

# abaixo, exemplo do walrus

print(nome := 'geek university')

# Resposta: geek university
# geek university

"""
# Abaixo, versão python 3.7
cesta = []
fruta = input('Informe a fruta: ')
while fruta != 'jaca':
    cesta.append(fruta)
    fruta = input('Informe a fruta: ')

print(cesta)

"""

# Abaixo, em python a partir 3.8

cesta = []
while (fruta := input("Informe a fruta: ")) != 'jaca':
    cesta.append(fruta)

print(f'A cesta foi preenchida com {cesta}')
