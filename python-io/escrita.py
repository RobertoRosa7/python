# -*- coding: UTF-8 -*-
arquivo_contato = open('contatos.csv', encoding='latin_1', mode='a')
contato = '12,Carol,carol@gmail.com.br\n'

arquivo_contato.write(contato)