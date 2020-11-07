### Intro

###### 01/11/2020

- Tipos de Variáveis
  - Numéricas
    - Contínua `números reais`
    - Discreta `números inteiros`
  - Categóricas `String`
    - Nominal `Dados não mensuráveis, exemplo: cor dos olhos, gênero, nome de pessoa etc..`
    - Ordinal `Sob ordenação, exemplo: tamanho, P, M e G`

### Pré-processamento com pandas e scikit-learn

###### 04/11/2020

- Tratamento de valores inconsistentes
- Tratamento de valores faltantes
- Escalonamento de atributos
- Base de dados do censo
- Transformação de variáveis categóricas

###### 05/11/2020

- Avaliação de algoritmos
- Divisão das bases de dados em treinamento e teste


### Aprendizagem Bayesiana
  - Naive bayes introdução
  - Naive bayes aprendizagem
  - Naive bayes classificação
  - Naive bayes correção laplaciana - corrigir valor com zero necessario adicionar um novo registro para fazer calculo
  - Naiva bayes com Scikit-learn
  - Calculo Risco Alto: `P(alto) = 6/14 * 1/6 * 4/6 * 6/6 * 1/6` resultado: 0,0079
  - Calculo Risco Moderado: `M(moderado) = 3/14 * 1/3 * 1/3 * 2/3 * 1/3` resultado: 0,0052
  - Calculo Risco Baixo: `B(baixo) = 5/14 * 3/5 * 2/5 * 3/5 * 5/5` resultado: 0,0514
  - Calculo Porcentagem: `Soma(0,0079 + 0,0052 + 0,0514)` resultado: 0,0645 equivale a 100%
  - Calculo Porcentagem Risco alto: `0,0079 / 0,0645 * 100 = 12,24%`
  - Calculo Porcentagem Moderado: `0,0052 / 0,0645 * 100 = 8,06%`
  - Calculo Porcentagem Baixo: `0,0514 / 0,0645 * 100 = 79,68%`