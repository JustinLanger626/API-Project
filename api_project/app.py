import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow, 
    QWidget, 
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton )
from PyQt6.QtGui import QPalette, QColor, QFont
import controller

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        title = QLabel("Hello")
        title.setFont(QFont("Calibri",20))

        button = QPushButton("get next movie")
        button.clicked.connect(self.getmovie)

        self.movie_text = QTextEdit()

        layout = QVBoxLayout()

        #add widgets
        layout.addWidget(title)
        layout.addWidget(button)
        layout.addWidget(self.movie_text)
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def getmovie(self):
        text = controller.next_mcu_movie()
        self.movie_text.setText(text)
        self.movie_text.toHtml()



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()