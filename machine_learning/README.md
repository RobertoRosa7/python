### Intro

- Tipos de aprendizagem de maquina
  - Naive bayes: gera um modelo que é a tabela de probabilidade
  - Decision tree: gera um modelo que é a árvore de decisão
  - Rule OneR: gera um modelo que é o conjunto de regras
  - KNN (k-nearest neighbour): gera uma instância que cálcula a distância dos registros

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
  - Modelo: Analise os dados e constroe uma tabela de probabilidade
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
  - Modelo: Analiza dos dados e constroe um árvore de decisão
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

###### 14/11/2020

- Árvores de decisão
  - Bias (viés)
  - Erros por classificação
  - Variânça
    - Erros por sensibilidade pequenas mudanças na base de treinamento
    - Overfitting - algoritmo se adapta demais ao registro de treinamento
  - Vantagens
    - Fácil interpretação
    - Não precisa de padronização ou normalização
    - Rápido para classificar novos registros
  - Desvantagens
    - Overfitting
    - Geração de árvores muito complexas
    - Pequenas mudanças na árvore
    - Problema NP-completo para construir a árvore
  - Random Forest `Kinect da Microsoft`
    - Melhoram o desempenho na árvore de decisção
  - CART - Classification And Regression Trees
- Árvores de decisão com scikit-learn
- Random forest
- Random forest com scikit-learn

###### 15/11/2020

### Aprendizagem por Regra

- Introdução a Regra
  - Modelo: Analisa os dados e constroe uma regra
- Indução de regras OneR
- Indução de regras algoritmo OneR I e OneR II
- Indução de regras algoritmo PRISM
- Classificador base - majority learner

###### 17/112020

### Aprendizagem baseada em instâncias

- Introdução KNN (k-nearest neighbour)
  - Modelo: Analisa os dados e armazena os exemplos de treinamento
- Cálculo de distâncias KNN (k-nearest neighbour)

  - Distância euclidiana: `DE(x,y) = Math.sqrt(Math.pow(v1[index] - v2[index], 2))`

    ```
      x = [5,7,9]
      y = [5,5,5]
      Subtração de cada posição do vetor
        5-5 = 0
        7-5 = 2
        9-5 = 4
      Elevação ao quadrado
        0² = 0
        2² = 4
        4² = 15
      Somatório
        0+4+16 = 20
      Raiz quadrada
        sqrt(20) = 4,47
    ```

    ```
      import math
      v1 = [5,7,9]
      v2 = [5,5,5]
      soma = 0

      for i in range(len(v1)):
        soma += math.pow(v1[i] - v2[i], 2)
      DE = math.sqrt(soma)
    ```

- Classificação KNN (k-nearest neighbour)
- Normalização e padronização KNN (k-nearest neighbour)

#### Referências complementares

> Livro Data Mining with Decision Trees: Theory and Applications (Machine Perception and Artificial Intelligence) de Oded Z. Maimon: livro de fácil compreensão e focado somente em árvores de decisão

> Livro C4.5: Programs for Machine Learning (Morgan Kaufmann Series in Machine Learning) de J. Ross Quinlan: um dos livros mais clássicos sobre o assunto

> Livro Decision Tress and Random Forests: A Visual Introduction For Begginers: A Simple Guide to Machine Learning With Decision Trees de Chris Smith e Mark Koning: um dos livros mais fáceis e didáticos sobre o assunto

> Livro Machine Learning With Random Forests And Decision Trees: A Visual Guide For Beginners de Scott Hartshorn: outro livro também muito didático

> Artigo Mineração de Dados com Árvores de Decisão de Jones Granatyr, Fábio Spak, Fabrício Enembreck e Otto Robert Lessing: artigo que fizemos para a revista Devmedia, que mostra a teoria a implementação prática de árvores de decisão no software Weka
