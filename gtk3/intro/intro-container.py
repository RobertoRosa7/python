# -*- coding: utf-8 -*-

import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

class MyBox(Gtk.Window):
  def __init__(self):
    Gtk.Window.__init__(self, title="Window Box")
    self.box = Gtk.Box(spacing=6)
    self.add(self.box)

    self.button1 = Gtk.Button(label="Entrar")
    self.button1.connect('clicked', self.on_clicked_button1)
    self.box.pack_start(self.button1, True, True, 0)

    self.button2 = Gtk.Button(label="Sair")
    self.button2.connect('clicked', self.on_clicked_button2)
    self.box.pack_start(self.button2, True, True, 0)

    # Enquanto com os widgets 
    # Gtk.Box.pack_start() estão posicionados da esquerda para a direita, 
    # Gtk.Box.pack_end() os posiciona da direita para a esquerda.

  def on_clicked_button1(self, widget):
    print("Access granted")
  
  def on_clicked_button2(self, widget):
    print("Access deny")


app = MyBox()
app.connect('destroy', Gtk.main_quit)
app.show_all()
Gtk.main()