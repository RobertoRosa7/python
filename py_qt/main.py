from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QBoxLayout, QVBoxLayout, QMainWindow
from PySide6.QtGui import QFont, QAction
from qdarktheme import load_stylesheet


app = QApplication()
app.setStyleSheet(load_stylesheet())

def callback():
  print('click no button')

class Window(QMainWindow):
  def __init__(self):
      super().__init__()
      self.base = QWidget()
      self.layout = QVBoxLayout()

      self.font = QFont()
      self.font.setPixelSize(90)

      self.label = QLabel('Deixe um like!')
      self.label.setFont(self.font)
      self.label.setAlignment(Qt.AlignCenter)

      self.button = QPushButton('Botão')
      self.button.setFont(self.font)
      self.button.clicked.connect(callback)

      self.layout.addWidget(self.label)
      self.layout.addWidget(self.button)

      self.base.setLayout(self.layout)

      self.setCentralWidget(self.base)

      self.menu = self.menuBar()
      self.file_menu = self.menu.addMenu('Menu')
      self.action = QAction('Print')
      self.action.triggered.connect(self.change_label)

      self.file_menu.addAction(self.action)


  def change_label(self):
    self.label.setText('Clicado')



main = Window()
main.show()
app.exec()