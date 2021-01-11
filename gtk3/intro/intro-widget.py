# -*- coding: utf-8 -*-

import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk


default_size = {'width': 320, 'height': 568}

class Window(Gtk.Window):
  def __init__(self):
    Gtk.Window.__init__(self, title="Window")

    self.set_default_size(default_size['width'], default_size['height'])
    label = Gtk.Label()
    label.set_label("This is a Basic Window")
    # # label.set_angle(50)
    # # label.set_halign(Gtk.Align.START) # print(dir(Gtk.Align))
    self.add(label)

class AboutDialog(Gtk.AboutDialog):
  def __init__(self):
    Gtk.AboutDialog.__init__(self)
    # self.set_default_size(default_size['width'], default_size['height'])

class AccelLabel(Gtk.AccelLabel):
  def __init__(self):
    Gtk.AccelLabel.__init__(self)

class ActionBar(Gtk.ActionBar):
  def __init__(self):
    Gtk.ActionBar.__init__(self)


class AppChooserButton(Gtk.AppChooserButton):
  def __init__(self):
    Gtk.AppChooserButton.__init__(self)


var = Window()
# var = AboutDialog()
# var = AppChooserButton()
var.connect("destroy", Gtk.main_quit)
var.show_all()
Gtk.main()