# -*- coding: utf-8 -*-

# THE LIST DATA TYPE
spam = ['cat', 'bat', 'dog', 'rat', 'elephant'] # simple array list
spamCompose = [['cat', 'bat'], ['dog', 'rat'], ['elephant']] # list compose
spam1 = ['cat', 'bat', 'dog', 'rat', 'elephant']

# DEL
# del spam1[1] # deletar

# ADD
# spam1_1 = spam + spam1 # somar array
# print(len(spam1_1)) # quantidade itens dentro do array

# CONVERT
numNumber = 1
numString = '1'
numFloat = 1
stringArray = 'hello world'
toString = str(numNumber) # converte numero para string
toNumber = int(numString) # converte string para numero
toFloat = float(numFloat) # converte para numeros reais
stringToArray = list(stringArray) # converte string em arrays

# SEARCH IN ARRAY IN AND NOT IN
# print('cats' in spam) # True or False
# print('cats' not in spam) # True or False


# print(spam1)
# INCLUDE VALUE IN ARRAY
# spam2 = [1,2,3]
# spam2[1] = 'Hello' # substituindo valor 2 (number) pelo Hello (string)
# spam3 = [1,3,'hello']
# spam3[1:3] = ['Toqui','Berlim','Rio'] # substituindo valor 3 e hello

# DEBUG
print(toString, '\n', toNumber, '\n', toFloat, '\n', stringToArray)
# print(spam1[:2]) # inicia do zero até posição 4, isto é, até rat
# print(spam1[2:]) # remove o primeiro e imprime o restante
# print(spam1[:-1]) # remove o último item e imprime o restante
# print(spam1[1:3]) # posição inicial:posição final
# print(spam1[:-1])
# print(spam3)
# print(spam2)
# print(spam) # acesso a lista completa
# print(spam[0]) # acesso a posição específica
# print(spamCompose) # acesso a lista completa
# print(spamCompose[0]) # acesso ao item na posição específica
# print(spamCompose[0][1]) # acesso ao valor do segundo array interno
# print(spam[-1]) # acesso ao último item da lista
# print(spamCompose[-1]) # acesso ao último array da lista
# print(spamCompose[-2]) # acesso ao penúltimo item da lista