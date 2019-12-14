# coding: utf8
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber
from PyQt5.QtGui import QPixmap
from PyQt5.Qt import QFont
import sys

class The_Main_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # создание окна размером 1000 х 750
        self.setGeometry(100, 100, 1000, 850)
        # окно нызывается "Читалка". По сути это - название программы
        self.setWindowTitle('ЧИТАЛКА')
        self.setStyleSheet("background-color: #66CDAA; color: #191970; font-family: Times; font-size: 29px")

        self.word_label = QLabel(self)
        self.word_label.setText("Введите слово: ")
        self.word_label.move(50, 70)

        self.word_input = QLineEdit(self)
        self.word_input.move(270, 55)
        self.word_input.resize(550, 50)

        self.btn = QPushButton('Нажми, когда введёшь слово', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(50, 120)
        self.btn.clicked.connect(self.give_info)
        self.btn.clicked.connect(self.transcription)

        self.label1 = QLineEdit(self)
        self.label1.setText("ТРАНСКРИПЦИЯ")
        self.label1.move(420, 450)
        self.label1.resize(550, 100)

        self.label_sl = QLineEdit(self)
        self.label_sl.setText("РАЗБИЕНИЕ НА СЛОГИ")
        self.label_sl.move(420, 550)
        self.label_sl.resize(550, 100)

        self.label_l = QLineEdit(self)
        self.label_l.setText("БУКВЫ В СЛОВЕ")
        self.label_l.move(420, 190)
        self.label_l.resize(550, 50)

        self.label_v = QLineEdit(self)
        self.label_v.setText("ГЛАСНЫЕ В СЛОВЕ")
        self.label_v.move(420, 240)
        self.label_v.resize(550, 50)

        self.label_c = QLineEdit(self)
        self.label_c.setText("СОГЛАСНЫЕ В СЛОВЕ")
        self.label_c.move(420, 290)
        self.label_c.resize(550, 50)

        self.label_an = QLineEdit(self)
        self.label_an.setText("ИНОЕ")
        self.label_an.move(420, 340)
        self.label_an.resize(550, 50)

        self.pixmap = QPixmap()
        self.image = QLabel(self)
        self.image.move(100, 300)
        self.image.resize(230, 200)
        self.image.setPixmap(self.pixmap)

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
                if w.isalpha() == False:
                    trnscrpt += w
    
        trnscrpt += ']'
        self.label1.setText("{}".format(trnscrpt))
        self.answer = trnscrpt


    def syllable(self):
        self.syllables = self.word_input.text().upper()
        self.label2.setText(self.syllables)


    def give_info(self):
        word_to_info = self.word_input.text().lower()
        # Если пользователь ввел неподходящее слово или фразу, то мы не транслитерируем и уведомляем его об этом (было в т.ч. до этого)
        if not all((symbol in [chr(i) for i in range(ord('а'), ord('я') + 1)] or symbol.isalpha() == False) for symbol in word_to_info):
        #if (symbol.lower() in 'qwertyuioplkjhgfdsazxcvbnm' or symbol in '1234567890-_=+*&^%$#@!~№;,<.>":?\/ |' for symbol in word_to_info):
            # self.label1.setText("Ой, что-то пошло не так, поробуйте снова...")
            self.label1.setText("Ой, что-то пошло не так, поробуйте снова...")
            self.label_l.setText("Ой, что-то пошло не так, поробуйте снова...")
            self.label_v.setText("Ой, что-то пошло не так, поробуйте снова...")
            self.label_c.setText("Ой, что-то пошло не так, поробуйте снова...")
            self.label_sl.setText("Ой, что-то пошло не так, поробуйте снова...")

            self.pixmap.load("kartinka_dlya_oshibki.jpg")
            self.image.setPixmap(self.pixmap)

        else:
            # Она сделана под цвет фона, и её не видно
            self.pixmap.load("kartinka_na_sluchay_ne_oshibki.jpg")
            self.image.setPixmap(self.pixmap)
            # self.image.resize(1, 1)
            # Непосредственно нахождение количества тех или иных букв в словах
            # Сначала создали список со всеми нужными буквами, чтобы не потерять их
            # self.label1.setText(self.answer)
            letters = [chr(i) for i in range(ord('а'), ord('я') + 1)]
            vowels = ['а', 'у', 'о', 'е', 'и', 'я', 'ю', 'ё', 'э', 'ы']
            cons = list('йцкнгшщзхждлрпвфчмстб')

            l = set([i for i in word_to_info if i in letters])
            v = set([i for i in word_to_info if i in vowels])
            c = set([i for i in word_to_info if i in cons])
            an = set([i for i in word_to_info if i not in c and i not in v and i != ' '])

            self.label_l.setText('Буквы в слове: {}'.format(sorted([i for i in l])))
            self.label_v.setText('Гласные в слове: {}'.format(sorted([i for i in v])))
            self.label_c.setText('Согласные в слове: {}'.format(sorted([i for i in c])))
            self.label_an.setText('Иные символы: {}'.format([i for i in an]))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = The_Main_Window()
    window.show()
    sys.exit(app.exec())