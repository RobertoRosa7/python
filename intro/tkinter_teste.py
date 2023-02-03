# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox

# nova instancia
tk = Tk()

# size of window
tk.geometry('600x400')

# função imprimir mensagem
def clique_aqui():
    msg = messagebox.showinfo('Curso de Python', 'Seja bem-vindo(a)')

# button
btn = Button(tk, text = 'Clique aqui', command = clique_aqui)

# position
btn.place(x=50, y=50)

# listen event
tk.mainloop()
