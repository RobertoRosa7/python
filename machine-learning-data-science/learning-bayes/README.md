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
