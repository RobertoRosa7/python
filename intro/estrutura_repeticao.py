# -*- coding: utf-8 -*-

"""
    Estrutura de Repetição: while e for
"""
# usando while
x = 1
while x < 10:
    # print(x)
    x += 1 # nessário para não travar em loop infinito

lista1 = [1,2,3,4,5]
lista2 = ['ola', 'mundo', '!']
lista3 = [0, 'ola', 'brasil', 'japão', 9.99, True]

# usando for
# for i in lista3:
#     print(i)

# range(indice, qtda, salto)
for i in range(10,20,2):
    print(i)
