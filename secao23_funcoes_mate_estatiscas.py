"""
Funções matemáticas e estatísticas
"""

import math
"""
# math.prod - Retorna o produto de um container numérico (uma caixinha onde se coloca números)

nuns_v1 = [2, 3, 6, 8]
nuns_v2 = (2, 3, 6, 8)
nuns_v3 = {2, 3, 6, 8}

print(math.prod(nuns_v1))  # o prod faz a conta de multiplicação
print(math.prod(nuns_v2))
print(math.prod(nuns_v3))

# Resposta:
# 288
# 288
# 288  (vezes)



# math.isqrt  -> Cálculo da raiz quadrada
print(math.isqrt(9))  # Raiz quadrada com numero inteiro
print(math.sqrt(9))  # Raiz quadrada com numero real
print(math.isqrt(17))
print(math.sqrt(17))


# 3
# 3.0
# 4
# 4.123105625617661

# math.dist  -> retorna a distancia euclidiana entre dois pontos (3d ou 2d)

# pontos 3d
p3d1 = (12, 50, 40)
p3d2 = (6, 7, 13)

# pontos 2d
p2d1 = [12, 50]
p2d2 = [6, 7]

print(math.dist(p3d1, p3d2))
print(math.dist(p2d1, p2d2))

# Resposta 51.12729212465687
# 43.41658669218482


# math.hypot  -> retorna a hipotenusa ou norma euclidiana

print(math.hypot(*p3d1))
print(math.hypot(*p2d1))

# Resposta:
# 65.14598989960932
# 51.419840528729765


# Estatísiticas

# statistics.fmean - -> calcula a media dos números reais

import statistics

valores_reais = [1.45, 6.789, 3.45, 89.98765]
valores_inteiros = [1, 6, 3, 89]

print(statistics.fmean(valores_reais))

print(statistics.fmean(valores_inteiros))

# Resposta: 25.4191625
# 24.75
"""

# statistics.geometric_mean  -> Calcula as Médias geometricas de números reais


import statistics

valores_reais = [1.45, 6.789, 3.45, 89.98765]
valores_inteiros = [1, 6, 3, 89]

print(statistics.geometric_mean(valores_reais))
print(statistics.geometric_mean(valores_inteiros))

# Resposta: 7.435222238889638
# 6.326530818100785

# statistics.multimode - retorna o valor mais frequente em uma sequência

seq1 = 'Geek University'
seq2 = [3, 5, 3, 8, 7, 9, 5, 3]
seq3 = [1, 2, 3, 1, 2, 3, 4, 5, 6]

print(statistics.multimode(seq1))
print(statistics.multimode(seq2))
print(statistics.multimode(seq3))

# Resposta: ['e']
# [3]
# [1, 2, 3]




