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
        # self.answer = self.word_input.text()[::-1]
        # self.label1.setText(self.answer)
        word = self.word_input.text()
        word = word.lower()

        d ={
            "а": "а", "б": ["б", "б'"], "в": ["в", "в'"], "г": ["г", "г'"],
            "д": ["д", "д'"], "е": ["э", "й'э"], "ё": ["о", "й'о"], "ж": "ж",
            "з": ["з", "з'"], "и": "и", "й": "й'", "к": ["к", "к'"], "л": ["л", "л'"],
            "м": ["м", "м'"], "н": ["н", "н'"], "о": "о", "п": ["п", "п'"],
            "р": ["р", "р'"], "с": ["с", "с'"], "т": ["т", "т'"], "у": "у",
            "ф": ["ф", "ф'"], "х": ["х", "х'"], "ц": "ц", "ч": "ч'", "ш": "ш",
            "щ": "щ'", "ы": "ы", "э": "э",  "ю": ["у", "й'у"],
            "я": ["а", "й'а"]
            }
    
        consonants = 'йцкнгшщзхждлрпвфчсмтб'
        vowels = 'ёуеэоаыяию'
        smth = 'ъь'
    
        trnscrpt = '['
        for i in range(len(word)):
            if word[i] in d:
                w = word[i]
        
                if w in vowels:
                    if w in 'уэоаыи':
                        trnscrpt += w
                    elif w in 'ёеяю':
                        if i == 0:
                            trnscrpt += d[w][1]
                        else:
                            if word[i - 1] in vowels or word[i - 1] in smth:
                                trnscrpt += d[w][1]
                            else:
                                trnscrpt += d[w][0]
    
                if w in consonants:
                    if w in 'йцшщжч':
                        trnscrpt += d[w]
                    else:
                        if i != len(word)-1 and word[i + 1] in 'ёеяиью':
                            trnscrpt += d[w][1]
                        else:
                            trnscrpt += d[w][0]
    
        trnscrpt += ']'
        self.answer = trnscrpt
        self.label1.setText(self.answer)

    def syllable(self):
        self.syllables = self.word_input.text().upper()
        self.label2.setText(self.syllables)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
