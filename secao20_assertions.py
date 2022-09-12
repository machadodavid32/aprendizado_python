"""
Assertions (Checagens/Questionamentos/Afirmações)

Em python utilizamos a palavra reservada 'assert' para realizar simples
afirmações utilizadas nos testes.

Utilizamos o 'assert' em uma expressão que queremos checar se é 
válida ou não. Se a expressão for verdadeira, retorna None e caso
seja falsa, levanta um erro do tipo AssertionError.

Obs: Nós podemos especificar, opcionalmente, um segundo argumento ou mesmo
uma mensagem de erro personalizada.

Obs: A palavra 'assert' pode ser utilizada em qualquer função ou codigo
nosso. Não precisa ser exclusivamente nos testes. 

# Alerta! Cuidado ao utilizar assert. Se um programa Python for executado
com o parâmetro -O, nenhum assertion será validado. Ou seja, todas as
suas validações ja eram.


"""

def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos numeros precisam ser positivos'
    return a + b

ret = soma_numeros_positivos(2, 4)  # resposta deve ser 6
#ret = soma_numeros_positivos(-2, 4)  # Aqui vai dar AsserTionError
#print(ret)
# Resposta: 6
# AssertionError: Ambos numeros precisam ser positivos     

def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'batata frita',
        'cachorro quente',
        ], 'A comida precisa ser fastfood'
    return f'Eu estou comendo {comida}'


comida = input("Informe a comida: ")
print(comer_fast_food(comida))


