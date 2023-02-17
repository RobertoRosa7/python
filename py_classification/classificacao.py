#-*- coding: UTF-8 -*-
porco1 =      [1, 1, 0]
porco2 =      [1, 1, 0]
porco3 =      [1, 1, 0]
cachorro =    [1, 1, 1]
cachorr2 =    [0, 1, 1]
cachorro3 =   [0, 1, 1]

dados = [porco1, porco2, porco3, cachorro, cachorr2, cachorro3]

marcacoes = [1, 1, 1, -1, -1, -1]
misterioso = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [0, 1, 1]

teste = [misterioso, misterioso2, misterioso3]
resultado_esperaco = [-1, 1, -1]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(dados, marcacoes)
resultado = modelo.predict(teste)
diferencas = resultado - resultado_esperaco
acertos = [d for d in diferencas if d==0]

print(f'total de acertos {len(acertos) / len(teste)}') 