import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow, 
    QWidget, 
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton,
    QHBoxLayout )
from PyQt6.QtGui import QPalette, QColor, QFont
import controller

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        #movie data
        self.movies = []
        self.next_release = ""
        self.current_movie_index = 0

        title = QLabel("Hello")
        title.setFont(QFont("Calibri",20))

        button_layout = QHBoxLayout()

        next_button = QPushButton("Next Movie")
        next_button.clicked.connect(self.getmovie)

        back_button = QPushButton("Previous Movie")
        back_button.clicked.connect(self.getprevious)

        button_layout.addWidget(back_button)
        button_layout.addWidget(next_button)

        self.movie_text = QTextEdit()

        layout = QVBoxLayout()

        #add widgets
        layout.addWidget(title)
        layout.addLayout(button_layout)
        layout.addWidget(self.movie_text)
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def getmovie(self):
        if self.movies: 
            if self.current_movie_index < len(self.movies):
                text, release_date = controller.next_mcu_movie(self.next_release)
            else: 
                text = self.movies[self.current_movie_index +1]
            self.current_movie_index += 1
        else:
            text, release_date = controller.next_mcu_movie()
        self.next_release = release_date
        self.movies.append(text)
        self.movie_text.setText(text)
        self.movie_text.toHtml()

    def getprevious(self): 
        if self.movies and self.current_movie_index > 0:
            text = self.movies[self.current_movie_index - 1]
            self.current_movie_index -= 1
            self.movie_text.setText(text)
            self.movie_text.toHtml()





app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()