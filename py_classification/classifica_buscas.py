from typing import Counter
from dados import carregar_buscas
import pandas as pd

x, y = carregar_buscas()

df = pd.read_csv('py_data/busca.csv')
y_df = df['comprou']
x_df = df[['home', 'busca', 'logado']]

x_dummies_df = pd.get_dummies(x_df)
y_dummies_df = y_df

x = x_dummies_df.values
y = y_dummies_df.values

porcentagem_treino = 0.8
porecentagem_teste = 0.1
tamanho_de_treino = int(porcentagem_treino * len(y))
tamanho_de_teste = int(porecentagem_teste * len(y))
tamanho_de_validacao = int(len(y) - tamanho_de_treino - tamanho_de_teste)

# 0 a 799
treino_x = x[0:tamanho_de_treino]
treino_y = y[0:tamanho_de_treino]

# 800 a 899
fim_teste = tamanho_de_treino + tamanho_de_teste
teste_x = x[tamanho_de_treino:fim_teste]
teste_y = y[tamanho_de_treino:fim_teste]

# 900 a 999
validacao_dados = x[fim_teste:]
validacao_teste = y[fim_teste:]

def fit_and_predict(name, modelo, treino_x, treino_y, teste_x, teste_y):
  modelo.fit(treino_x, treino_y)
  resultado = modelo.predict(teste_x)
  # diferencas = resultado - teste_y
  # acertos = [d for d in diferencas if d == 0]
  acertos = (resultado == teste_y)
  total_acertos = sum(acertos)
  total_elementos = len(teste_y)
  taxa_acertos = 100.0 * total_acertos / total_elementos
  print("Taxa de acerto {1} - {0}".format(name, taxa_acertos))
  return taxa_acertos



from sklearn.naive_bayes import MultinomialNB
modelo_multinomialnb = MultinomialNB()
resultado_multinomialnb = fit_and_predict('MultinomialNB',modelo_multinomialnb, treino_x, treino_y, teste_x,teste_y)

from sklearn.ensemble import AdaBoostClassifier
modelo_adaboost = AdaBoostClassifier()
resultado_adaboost = fit_and_predict('AdaBoostClassifier', modelo_adaboost, treino_x, treino_y,teste_x,teste_y)

if resultado_multinomialnb > resultado_adaboost:
  vencedor = modelo_multinomialnb
  name = 'MultinomialNB'
else:
  vencedor = modelo_adaboost
  name = 'AdaBoostClassifier'
  
resultado = vencedor.predict(validacao_dados)
acertos = (resultado == validacao_teste)
total_de_acerto = sum(acertos)
total_de_elementos = len(validacao_teste)
taxa_de_acerto = 100.0 * total_de_acerto / total_de_elementos

acerto_base = max(Counter(validacao_teste).values())
taxa_de_acerto_base = 100.0 * acerto_base / len(validacao_teste)

print("Taxa de acerto base %f" %taxa_de_acerto_base)
print("Total de teste %d" %len(validacao_dados))
print("Taxa de acerto do vencedor no mundo real com: {0} - ({1}) ".format(taxa_de_acerto, name))