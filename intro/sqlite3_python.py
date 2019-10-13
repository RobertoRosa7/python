# -*- coding: utf-8 -*-

import sqlite3

db = sqlite3.connect('database.db')
c = db.cursor()
c.execute('create table portfolio (symbol text, shares integer, price real)')
db.commit()

# criando dados para inserção no banco de dados
stocks = [
  ('Iphone plus', 100, 2999.99), 
  ('Macbook air', 200, 5999.99),
  ('SamSung', 300, 1999.49)
]

# inserindo dados no banco
c.executemany('insert into portfolio values(?,?,?)', stocks)
db.commit()

# imprindo resultado
for row in db.execute('select * from portfolio'):
  print(row)