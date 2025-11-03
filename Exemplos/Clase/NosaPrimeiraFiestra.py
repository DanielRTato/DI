from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QLayout)
import sys

class NosaPrimeiraFiestra (QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Ventana con QT") # Nombre de la ventana
		#self.setFixedSize(800, 600)  # Fija el tamaño de la venta
		self.setMinimumSize(400, 400) # Tamaño mínimo de la pantalla (horizontal, vertical)

		self.txtSaudo = QLineEdit(self)
		self.lblEtiqueta = QLabel("etiqueta", self)
		fonte = self.lblEtiqueta.font()
		fonte.setPointSize(7)
		self.lblEtiqueta.setFont(fonte)
		self.lblEtiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)

		self.show()
		#self.hide()

if __name__ == "__main__":
	aplicacion = QApplication(sys.argv)
	fiestra = NosaPrimeiraFiestra()
	aplicacion.exec()