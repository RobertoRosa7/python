# -*- coding: utf-8 -*-

"""
    Input - entrada de dados pelo usuário
"""
# name = input('digite seu nome: ')
# print('Seja Bem Vindo(a) ' + name)


"""
    Concatenação e filtro de string
"""
a = 'roberto'
b = 'rosa'
nome = a +" "+ b + '\n'
# print(nome) nome completo

# filtro 0: posição inicial, 2: quantidade
# print(nome[0:5])
# print('maiúsculo', nome.upper()) # nome maiúsculo
# print('minúsculo', nome.lower()) # nome minúsculo


"""
    Removendo espaço no início e no final e caracteres especiais: strip()
"""
filterName = nome.strip()
# print('nome filtrado: ', filterName)

"""
    Convertendo string em lista: split()
"""
seq = 'abc def ghi jkm lmn opq rst'
strToArray = seq.split(' ')
# print('str to array: ', strToArray)

"""
    Procura por substrings: find()
"""
# retorna o indice da string - se não encontrar retorna -1
search = seq.find("vovo")
# print(search)


"""
    Substituir strings ou caracteres: replace()
"""
subName = seq.replace('rst', 'Roberto Rosa')
print(subName)
