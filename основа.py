from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLineEdit,QLabel,QLCDNumber
from PyQt5.QtGui import QPixmap
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        # создание окна размером 1000 х 750
        self.setGeometry(100, 100, 1000, 750)
        # окно нызывается "Читалка". По сути это - название программы
        self.setWindowTitle('ЧИТАЛКА')
        self.setStyleSheet("background-color: #66CDAA; color: #191970; font-family: Times; font-size: 29px")

        self.word_label = QLabel(self)
        self.word_label.setText("Введите слово: ")
        self.word_label.move(50, 70)

        self.word_input = QLineEdit(self)
        self.word_input.move(270, 55)
        self.word_input.resize(550, 50)

        self.btn = QPushButton('Нажмите, когда введёте слово', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(50, 120)
        self.btn.clicked.connect(self.transcription)
        self.btn.clicked.connect(self.syllable)

        self.label1 = QLineEdit(self)
        self.label1.setText("ЗДЕСЬ БУДЕТ ТРАНСКРИПЦИЯ")
        self.label1.move(420, 370)
        self.label1.resize(550, 100)

        self.label2 = QLineEdit(self)
        self.label2.setText("ЗДЕСЬ БУДЕТ РАЗБИЕНИЕ НА СЛОГИ")
        self.label2.move(420, 500)
        self.label2.resize(550, 100)

        self.label3 = QLineEdit(self)
        self.label3.move(50, 200)
        self.label3.resize(300, 400)
        self.label3.setText("ИНСТРУКЦИЯ")

        self.label4 = QLineEdit(self)
        self.label4.move(420, 200)
        self.label4.resize(550, 100)
        self.label4.setText("МЕСТО ДЛЯ АУДИОФАЙЛА")

    def transcription(self):
        self.answer = self.word_input.text()[::-1]
        self.label1.setText(self.answer)

    def syllable(self):
        self.syllables = self.word_input.text().upper()
        self.label2.setText(self.syllables)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())