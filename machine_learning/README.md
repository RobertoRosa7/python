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

###### 12/11/2020

### Aprendizam por árvore de decisão

- Intro
- Intro árvore de decisão
  - identificar qual coluna da base de dados será responsável por ser a classe, depois contar quantas
    vezes de repete os atributos dividindo pelo total de atributos da classe... no caso da base de dados de risco de crédito a coluna de risco contem `total de 14 atributos sendo 6 de risco alto, 3 moderado e 5 baixo ficando`
    - risco alto: 6/14
    - risco moderado: 3/14
    - risco baixo: 5/14
  - Entropia - saber a relevancia de cada atributo da classe
  - Cálculo da entropia: `E(s) = -6/14 * log(6/14;2) - 3/14 * log(3/14;2) - 5/14 * log(5/14;2)`
  - Resultado da entropia geral: 1,53
  - Cálculo ganho da informação `Gain(S, A) = Entropy(S)`
    - G(atributo_historia) = `1,53-(5/14*1,37)-(5/14*1,52)-(4/14*0,81)` = 0,26
      - boa: (`5/14`) `-1/5*log(1/5;2)-1/5*log(1/5;2)-3/5*log(3/5;2)` = 1,37
        - alto: (`1/5`)
        - moderado: (`1/5`)
        - baixo: (`3/5`)
      - desconhecida: (`5/14`) `-2/5*log(2/5;2)-1/5*log(2/5;2)-2/5*log(2/5;2)` = 1,52
        - alto: (`2/5`)
        - moderado: (`2/5`)
        - baixo: (`2/5`)
      - ruim: (`4/14`) `-3/4*log(3/4;2)-1/4*log(1/4;2)` = 0,81
        - alto: (`3/4`)
        - moderado: (`1/4`)
        - baixo: (`0`)
    - G(atributo_divida) = `1,53-(7/14*1,38)-(7/14*1,56)` = 0,06
      - alta: (`7/14`) `-4/7*log(4/7;2)-1/7*log(1/7;2)-2/7*log(2/7;2)` = 1,38
        - alto: (`4/7`)
        - moderado: (`1/7`)
        - baixo: (`2/7`)
      - baixa: (`7/14`) `-2/7*log(2/7;2)-2/7*log(2/7;2)-3/7*log(3/7;2)` = 1.56
        - alto: (`2/7`)
        - moderado: (`2/7`)
        - baixo: (`3/7`)
    - G(atributo_garantia) = `1,53-(11/14*1,44)-(3/14*0,92)` = 0,20
      - nenhuma: (`11/14`) `-6/11*log(6/11;2)-2/11*log(6/11;2)-3/11*log(3/11;2)` = 1,44
        - alto: (`6/11`)
        - moderado: (`2/11`)
        - baixo: (`3/11`)
      - adequada: (`3/14`) `-0*log(0;2)-1/3*log(1/3;2)-2/3*log(2/3;2)` = 0,92
        - alto: (`0`)
        - moderado: (`1/3`)
        - baixo: (`2/3`)
    - G(atributo_renda) `1,53-(3/14*0)-(4/14*1,00)-(7/14*1,15)` = 0,66
    - menor que 35: (3/14) `-3/3*log(3/3;2)-0*log(0;2)-0*log(0;2)` = 0,00
      - alto: `(3/3)`
      - moderado: `(0)`
      - baixo: `(0)`
    - igual ou maior que 35 e menor que 35: `(4/14)` `-2/4*log(2/4;2)-2/4*log(2/4;2)-0*log(0;2)` = 1,00
      - alto: `(2/4)`
      - moderado: `(2/4)`
      - baixo: `(0)`
    - maior que 35: `(7/14)` `-1/7*log(1/7;2)-1/7*log(1/7;2)-5/7*log(5/7;2)` = 1,15
      - alto: `(1/7)`
      - moderado: `(1/7)`
      - baixo: `(5/7)`
    - resultado:
      - Histórico: `(0,26)`
      - Dívida: `(0,06)`
      - Garantias: `0,20`
      - Renda: `0,66`
- Árvores de decisão com scikit-learn
- Random forest
- Random forest com scikit-learn
