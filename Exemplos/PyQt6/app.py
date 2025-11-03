import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDial,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QSlider,
    QSpinBox,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        etiqueta = QLabel("1")
        #etiqueta.setText("Hola")
        font = etiqueta.font()
        font.setPointSize(30)
        etiqueta.setFont(font)
        etiqueta.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )

        self.setCentralWidget(etiqueta)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()