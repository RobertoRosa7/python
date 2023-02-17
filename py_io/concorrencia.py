# -*- coding: UTF-8 -*-
arquivo1 = open('contatos.csv', encoding='latin_1', mode='w')
arquivo2 = open('contatos.csv', encoding='latin_1', mode='w')

carol = '13,Caral,carol@gmail.com.br\n'
andreza = '14,Andreza,andreza@gmail.com.br\n'

arquivo1.write(carol)
arquivo2.write(andreza)

arquivo1.close()
arquivo2.close()