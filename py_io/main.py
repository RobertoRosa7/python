# -*- coding: UTF-8 -*-
import lista_contatos
try:
  contatos = lista_contatos.csv_para_contatos('contatos.csv')
  # lista_contatos.contatos_para_pickle(contatos, 'contatos.p')
  lista_contatos.contatos_para_json(contatos, 'contatos.json')

  for contato in contatos:
    print(f'{contato.id} - {contato.nome} - {contato.email}')

  # with open('contatos.csv', encoding='latin_1') as arquivo_contato:
  #   for line in arquivo_contato:
  #     print(line, end='')
except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permissão de escrita')