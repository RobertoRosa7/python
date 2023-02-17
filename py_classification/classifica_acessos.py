#-*- coding: UTF-8 -*-
from dados import carregar_acessos
from sklearn.naive_bayes import MultinomialNB

x,y = carregar_acessos()
treino_dados = x[:90]
treino_marcacoes = y[:90]

teste_dados = x[-9:]
teste_marcacoes = y[-9:]

modelo = MultinomialNB()
modelo.fit(treino_dados, treino_marcacoes)
# print(modelo.predict([[1,0,1], [0,1,0], [1,0,0], [1,1,1]]))
resultado = modelo.predict(teste_dados)
diferenca = resultado - teste_marcacoes
acertos = [d for d in diferenca if d == 0]
total_de_acertos = len(acertos)
total_de_elementos = len(x)
taxa_acertos = 100.0 * total_de_acertos / total_de_elementos

print(taxa_acertos)
