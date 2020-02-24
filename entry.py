from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber
from PyQt5.QtGui import QPixmap
import sys


class Beginning(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 1800, 950)
        self.setWindowTitle('РАЗБИРАЙКА')
        self.setStyleSheet("background-color: #7FFFD4; color: #008B8B; font-family: Arial; font-style: normal; font-size: 20pt; font-weight: bold")

        self.pixmap = QPixmap()
        self.image = QLabel(self)
        self.image.move(645, 0)
        self.image.resize(555, 450)
        self.image.setPixmap(self.pixmap)
        self.pixmap.load("entry.png")
        self.image.setPixmap(self.pixmap)

        self.pixmap_2 = QPixmap()
        self.image_2 = QLabel(self)
        self.image_2.move(0, 400)
        self.image_2.resize(555, 450)
        self.image_2.setPixmap(self.pixmap_2)
        self.pixmap_2.load("entry 2.2.png")
        self.image_2.setPixmap(self.pixmap_2)

        self.pixmap_3 = QPixmap()
        self.image_3 = QLabel(self)
        self.image_3.move(1225, 400)
        self.image_3.resize(555, 450)
        self.image_3.setPixmap(self.pixmap_3)
        self.pixmap_3.load("entry 3.png")
        self.image_3.setPixmap(self.pixmap_3)

        self.butt = QPushButton('НАЧАТЬ!', self)
        self.butt.setStyleSheet("background-color: #EEE8AA; color: #008080; font-family: Arial; font-style: normal; font-size: 20pt; font-weight: bold")
        self.butt.resize(400, 200)
        self.butt.move(715, 500)
        self.butt.clicked.connect(self.destroy_beginning)

    def destroy_beginning(self):
        self.image.resize(0, 0)
        self.image_2.resize(0, 0)
        self.image_3.resize(0, 0)
        self.butt.resize(0, 0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Beginning()
    ex.show()
    sys.exit(app.exec())
