
from py_kivy.uix.boxlayout import BoxLayout
from py_kivy.uix.behaviors import ToggleButtonBehavior
from py_kivy.properties import StringProperty


class MainWindow(BoxLayout):
    def __init__(self, **kw):
        super().__init__(**kw)


class NavTab(ToggleButtonBehavior, BoxLayout):
    text = StringProperty("")
    icon = StringProperty("")
    icon_active  = StringProperty("")

    def __init__(self, **kw):
        super().__init__(**kw)
