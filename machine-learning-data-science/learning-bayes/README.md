# Introdução

- Abordagem probabilística (Teorema de Bayes)
- Exemplos:
  - Filtros de Spam de E-mails
  - Mineração de emoção
  - Separação de documentos

## Base original de Risco de Crédito

| História do crédito | Dívida | Garantias | Renda anual         | `Risco`    |
| ------------------- | ------ | --------- | ------------------- | ---------- |
| Ruim                | Alta   | Nenhuma   | < 15.00             | `Alto`     |
| Desconhecida        | Alta   | Nenhuma   | >= 15.00 a <= 35.00 | `Alto`     |
| Desconhecida        | Baixa  | Nenhuma   | >= 15.00 a <= 35.00 | `Moderado` |
| Desconhecida        | Baixa  | Nenhuma   | > 35.00             | `Alto`     |
| Desconhecida        | Baixa  | Nenhuma   | > 35.00             | `Baixo`    |
| Desconhecida        | Baixa  | Adequada  | > 35.00             | `Baixo`    |
| Ruim                | Baixa  | Adequada  | > 35.00             | `Alto`     |
| Ruim                | Baixa  | Nenhuma   | < 15.00             | `Moderado` |
| Boa                 | Alta   | Adequada  | > 35.00             | `Baixo`    |
| Boa                 | Alta   | Nenhuma   | > 35.00             | `Baixo`    |
| Boa                 | Alta   | Nenhuma   | < 15.00             | `Alto`     |
| Boa                 | Alta   | Nenhuma   | >= 15.00 a <= 35.00 | `Moderado` |
| Boa                 | Alta   | Nenhuma   | < 35.00             | `Baixo`    |
| Ruim                | Alta   | Nenhuma   | >= 15.00 a <= 35.00 | `Alto`     |

## Naive Bayes

|                               | Boa | Desconhecida | Ruim | Alta | Baixo | Nenhuma | Adequada | < 15.00 | >= 15.00 a <= 35.00 | > 35.00 |
| ----------------------------- | --- | ------------ | ---- | ---- | ----- | ------- | -------- | ------- | ------------------- | ------- |
| Risco de crédito </br> classe | 5   | 5            | 4    | 7    | 7     | 11      | 3        | 3       | 4                   | 7       |
| Alto </br>6/14                | 1/6 | 2/6          | 3/6  | 4/6  | 2/6   | 6/6     | 0        | 3/6     | 2/6                 | 1/6     |
| Moderado </br>3/14            | 1/3 | 1/3          | 1/3  | 1/3  | 2/3   | 2/3     | 1/3      | 0       | 2/3                 | 1/3     |
| Baixo </br>5/15               | 3/5 | 2/5          | 0    | 2/5  | 3/5   | 3/5     | 2/5      | 0       | 0                   | 5/5     |
