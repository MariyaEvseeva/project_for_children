# coding: utf8
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber
from PyQt5.QtGui import QPixmap
from PyQt5.Qt import QFont
import sys
import pymorphy2
import random

class Beginning(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 50, 1800, 950)
        self.setWindowTitle('РАЗБИРАЙКА')
        self.setStyleSheet("background-color: #7FFFD4")
    
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
        self.close()
        self.MainWindow = The_Main_Window()
        self.MainWindow.show()


class The_Main_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 50, 1900, 1000)
        self.setWindowTitle('РАЗБИРАЙКА')
        self.setStyleSheet("background-color: #7FFFD4; color: #008B8B; font-family: Arial; font-style: normal; font-size: 16pt; font-weight: bold")

        self.pixmap_name = QPixmap()
        self.image_name = QLabel(self)
        self.image_name.move(770, 5)
        self.image_name.resize(407, 50)
        self.image_name.setPixmap(self.pixmap_name)
        self.pixmap_name.load("instead_of_name.png")
        self.image_name.setPixmap(self.pixmap_name)

        self.pixmap_angle = QPixmap()
        self.image_angle = QLabel(self)
        self.image_angle.move(1580, 700)
        self.image_angle.resize(370, 370)
        self.image_angle.setPixmap(self.pixmap_angle)
        self.pixmap_angle.load("angle.png")
        self.image_angle.setPixmap(self.pixmap_angle)

        self.pixmap_angle2 = QPixmap()
        self.image_angle2 = QLabel(self)
        self.image_angle2.move(1050, 670)
        self.image_angle2.resize(500, 406)
        self.image_angle2.setPixmap(self.pixmap_angle2)
        self.pixmap_angle2.load("angle 2.png")
        self.image_angle2.setPixmap(self.pixmap_angle2)

        self.word_label = QLabel(self)
        self.word_label.setText("Введи слово:")
        self.word_label.move(50, 80)

        self.word_input = QLineEdit(self)
        self.word_input.move(270, 70)
        self.word_input.resize(550, 50)

        self.btn = QPushButton('Нажми, когда введёшь слово', self)
        self.btn.resize(430, 40)
        self.btn.move(50, 130)
        self.btn.setStyleSheet("background-color: #40E0D0; color: #008080")
        self.btn.clicked.connect(self.give_info)
        self.btn.clicked.connect(self.transcription)

        self.label1 = QLineEdit(self)
        self.label1.setText("ТРАНСКРИПЦИЯ")
        self.label1.move(420, 390)
        self.label1.resize(570, 50)

        self.label_l = QLineEdit(self)
        self.label_l.setText("БУКВЫ В СЛОВЕ")
        self.label_l.move(420, 190)
        self.label_l.resize(570, 50)

        self.label_v = QLineEdit(self)
        self.label_v.setText("ГЛАСНЫЕ В СЛОВЕ")
        self.label_v.move(420, 240)
        self.label_v.resize(570, 50)

        self.label_c = QLineEdit(self)
        self.label_c.setText("СОГЛАСНЫЕ В СЛОВЕ")
        self.label_c.move(420, 290)
        self.label_c.resize(570, 50)

        self.label_an = QLineEdit(self)
        self.label_an.setText("ИНОЕ")
        self.label_an.move(420, 340)
        self.label_an.resize(570, 50)

        self.btn_2 = QPushButton('Нажми, чтобы посмотреть морфологические признаки', self)
        self.btn_2.resize(840, 50)
        self.btn_2.move(1050, 120)
        self.btn_2.setStyleSheet("background-color: #40E0D0; color: #008080")
        self.btn_2.clicked.connect(self.give_info_about_word)

        self.label_morph1 = QLineEdit(self)
        self.label_morph1.setText("")
        self.label_morph1.move(1050, 190)
        self.label_morph1.resize(840, 50)

        self.label_morph2 = QLineEdit(self)
        self.label_morph2.setText("")
        self.label_morph2.move(1050, 240)
        self.label_morph2.resize(840, 50)

        self.label_morph3 = QLineEdit(self)
        self.label_morph3.setText("")
        self.label_morph3.move(1050, 290)
        self.label_morph3.resize(840, 50)

        self.label_morph4 = QLineEdit(self)
        self.label_morph4.setText("")
        self.label_morph4.move(1050, 340)
        self.label_morph4.resize(840, 50)

        self.label_morph5 = QLineEdit(self)
        self.label_morph5.setText("")
        self.label_morph5.move(1050, 390)
        self.label_morph5.resize(840, 50)

        self.label_morph6 = QLineEdit(self)
        self.label_morph6.setText("")
        self.label_morph6.move(1050, 440)
        self.label_morph6.resize(840, 50)

        self.label_morph7 = QLineEdit(self)
        self.label_morph7.setText("")
        self.label_morph7.move(1050, 490)
        self.label_morph7.resize(840, 50)

        self.label_morph8 = QLineEdit(self)
        self.label_morph8.setText("")
        self.label_morph8.move(1050, 540)
        self.label_morph8.resize(840, 50)

        self.label_morph9 = QLineEdit(self)
        self.label_morph9.setText("")
        self.label_morph9.move(1050, 590)
        self.label_morph9.resize(840, 50)

        self.label_morph10 = QLineEdit(self)
        self.label_morph10.setText("")
        self.label_morph10.move(1050, 640)
        self.label_morph10.resize(840, 50)

        self.pixmap = QPixmap()
        self.image = QLabel(self)
        self.image.move(50, 180)
        self.image.resize(359, 288)
        self.image.setPixmap(self.pixmap)
        self.pixmap.load("standart.png")
        self.image.setPixmap(self.pixmap)

        self.btn_3 = QPushButton('Нажми, чтобы сделать фонетической разбор уникальных звуков', self)
        self.btn_3.resize(945, 50)
        self.btn_3.move(50, 490)
        self.btn_3.setStyleSheet("background-color: #40E0D0; color: #008080")
        self.btn_3.clicked.connect(self.phonetics)

        self.label_sounds1 = QLineEdit(self)
        self.label_sounds1.setText("")
        self.label_sounds1.move(50, 570)
        self.label_sounds1.resize(945, 40)

        self.label_sounds2 = QLineEdit(self)
        self.label_sounds2.setText("")
        self.label_sounds2.move(50, 610)
        self.label_sounds2.resize(945, 40)

        self.label_sounds3 = QLineEdit(self)
        self.label_sounds3.setText("")
        self.label_sounds3.move(50, 650)
        self.label_sounds3.resize(945, 40)

        self.label_sounds4 = QLineEdit(self)
        self.label_sounds4.setText("")
        self.label_sounds4.move(50, 690)
        self.label_sounds4.resize(945, 40)

        self.label_sounds5 = QLineEdit(self)
        self.label_sounds5.setText("")
        self.label_sounds5.move(50, 730)
        self.label_sounds5.resize(945, 40)

        self.label_sounds6 = QLineEdit(self)
        self.label_sounds6.setText("")
        self.label_sounds6.move(50, 770)
        self.label_sounds6.resize(945, 40)

        self.label_sounds7 = QLineEdit(self)
        self.label_sounds7.setText("")
        self.label_sounds7.move(50, 810)
        self.label_sounds7.resize(945, 40)

        self.label_sounds8 = QLineEdit(self)
        self.label_sounds8.setText("")
        self.label_sounds8.move(50, 850)
        self.label_sounds8.resize(945, 40)

        self.label_sounds9 = QLineEdit(self)
        self.label_sounds9.setText("")
        self.label_sounds9.move(50, 890)
        self.label_sounds9.resize(945, 40)

        self.label_sounds10 = QLineEdit(self)
        self.label_sounds10.setText("")
        self.label_sounds10.move(50, 930)
        self.label_sounds10.resize(945, 40)

        self.label_sounds11 = QLineEdit(self)
        self.label_sounds11.setText("")
        self.label_sounds11.move(50, 970)
        self.label_sounds11.resize(945, 40)

    def transcription(self):
        word = self.word_input.text()
        word = word.lower().strip()

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
            if word[i].isalpha() == False:
                trnscrpt = '['
                break
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
        if trnscrpt == '[]':
            trnscrpt = ''
        self.label1.setText("{}".format(trnscrpt))
        self.answer = trnscrpt


    def give_info(self):
        self.label_morph1.setText("")
        self.label_morph2.setText("")
        self.label_morph3.setText("")
        self.label_morph4.setText("")
        self.label_morph5.setText("")
        self.label_morph6.setText("")
        self.label_morph7.setText("")
        self.label_morph8.setText("")
        self.label_morph9.setText("")
        self.label_morph10.setText("")
        self.label_sounds1.setText('')
        self.label_sounds2.setText('')
        self.label_sounds3.setText('')
        self.label_sounds4.setText('')
        self.label_sounds5.setText('')
        self.label_sounds6.setText('')
        self.label_sounds7.setText('')
        self.label_sounds8.setText('')
        self.label_sounds9.setText('')
        self.label_sounds10.setText('')
        self.label_sounds11.setText('')
        word_to_info = self.word_input.text().lower().strip()

        if len([1 for symbol in word_to_info if symbol in [chr(i) for i in range(ord('a'), ord('z') + 1)]]) != 0:
            self.label_l.setText("Это иностранное слово!")
            self.label_v.setText("")
            self.label_c.setText("")
            self.label_an.setText("")
            self.label_morph1.setText("Это иностранное слово!")
            self.label_morph2.setText("")
            self.label_morph3.setText("")
            self.label_morph4.setText("")
            self.label_morph5.setText("")
            self.label_morph6.setText("")
            self.label_morph7.setText("")
            self.label_morph8.setText("")
            self.label_morph9.setText("")
            self.label_morph10.setText("")
            self.label_sounds1.setText('Это иностранное слово!')
            self.label_sounds2.setText('')
            self.label_sounds3.setText('')
            self.label_sounds4.setText('')
            self.label_sounds5.setText('')
            self.label_sounds6.setText('')
            self.label_sounds7.setText('')
            self.label_sounds8.setText('')
            self.label_sounds9.setText('')
            self.label_sounds10.setText('')
            self.label_sounds11.setText('')            

            pict = random.choice(["mistake.png", "mistake 2.png", "mistake 3.png"])
            self.pixmap.load(pict)
            self.image.setPixmap(self.pixmap)

        elif word_to_info == '':
            self.label_l.setText("")
            self.label_v.setText("")
            self.label_c.setText("")
            self.label_an.setText("")
            self.label_morph1.setText("")
            self.label_morph2.setText("")
            self.label_morph3.setText("")
            self.label_morph4.setText("")
            self.label_morph5.setText("")
            self.label_morph6.setText("")
            self.label_morph7.setText("")
            self.label_morph8.setText("")
            self.label_morph9.setText("")
            self.label_morph10.setText("")
            self.label_sounds1.setText('')
            self.label_sounds2.setText('')
            self.label_sounds3.setText('')
            self.label_sounds4.setText('')
            self.label_sounds5.setText('')
            self.label_sounds6.setText('')
            self.label_sounds7.setText('')
            self.label_sounds8.setText('')
            self.label_sounds9.setText('')
            self.label_sounds10.setText('')
            self.label_sounds11.setText('')

            self.pixmap.load('empty string.png')
            self.image.setPixmap(self.pixmap)

        else:
            self.pixmap.load("standart.png")
            self.image.setPixmap(self.pixmap)

            letters = [chr(i) for i in range(ord('а'), ord('я') + 1)]
            vowels = ['а', 'у', 'о', 'е', 'и', 'я', 'ю', 'ё', 'э', 'ы']
            cons = list('йцкнгшщзхждлрпвфчмстб')

            l = set([i for i in word_to_info if i in letters])
            v = set([i for i in word_to_info if i in vowels])
            c = set([i for i in word_to_info if i in cons])
            an = set([i for i in word_to_info if i not in c and i not in v and i != ' '])
            
            if len(l) != 0:
                self.label_l.setText('Буквы в слове: {}'.format(', '.join(sorted([i for i in l]))))
            else:
                self.label_an.setText('Букв нет')
            if len(v) != 0:
                self.label_v.setText('Гласные в слове: {}'.format(', '.join(sorted([i for i in v]))))
            else:
                self.label_v.setText('Гласных нет')
            if len(c) != 0:
                self.label_c.setText('Согласные в слове: {}'.format(', '.join(sorted([i for i in c]))))
            else:
                self.label_c.setText('Согласных нет')
            if len(an) != 0:
                self.label_an.setText('Иные символы: {}'.format(', '.join([i for i in an])))
            else:
                self.label_an.setText('Иных символов нет')
            
            if len([i for i in word_to_info if i in '`~1234567890!@#$%^&*()_ -+=\|]}[{;:"/?.><,' or i == "'"]) != 0:
                self.label_morph1.setText("Введи текст без точек, запятых и других символов!")
                self.label_morph2.setText("")
                self.label_morph3.setText("")
                self.label_morph4.setText("")
                self.label_morph5.setText("")
                self.label_morph6.setText("")
                self.label_morph7.setText("")
                self.label_morph8.setText("")
                self.label_morph9.setText("")
                self.label_morph10.setText("")
                self.label_sounds1.setText('Введи текст без точек, запятых и других символов!')
                self.label_sounds2.setText('')
                self.label_sounds3.setText('')
                self.label_sounds4.setText('')
                self.label_sounds5.setText('')
                self.label_sounds6.setText('')
                self.label_sounds7.setText('')
                self.label_sounds8.setText('')
                self.label_sounds9.setText('')
                self.label_sounds10.setText('')
                self.label_sounds11.setText('')

    def give_info_about_word(self):
        word = self.word_input.text()
        word = word.lower().strip()
        morph = pymorphy2.MorphAnalyzer()
        show = []
        p = morph.parse(word)[0]
        poses = {'VERB': 'глагол', 'NOUN': 'имя существительное', 'ADJF': 'имя прилагательное',
                 'ADJS': 'имя прилагательное', 'INFN': 'глагол (инфинитив)', 
                 'PRTF': 'причастие (полное)', 'PRTS': 'причастие (краткое)', 'GRND': 'деепричастие',
                 'NUMR': 'числительное', 'ADVB': 'наречие', 'NPRO': 'местоимение', 
                 'PREP': 'предлог', 'CONJ': 'союз', 'PRCL': 'частица', 'INTJ': 'междометие'}
        if p.tag.POS in poses:
            show.append(poses[p.tag.POS])
        else:
            return 'не определено'

        if show[0] == 'имя существительное':
            # определение падежа
            padezh = p.tag.case
            cases = {'nomn': 'именительный падеж', 'gent': 'родительный падеж', 'datv': 'дательный падеж',
                     'accs': 'винительный падеж', 'ablt': 'творительный падеж', 'loct': 'предложный падеж',
                     'voct': 'звательный падеж'}
            if padezh in cases:
                show.append(cases[padezh])
            else:
                show.append('падеж не определён')

            # определение числа
            numer = p.tag.number
            numbers = {'sing': 'единственное число', 'plur': 'множественное число',
                       'only sing': 'только единственное число', 'only plur': 'только множественное число'}
            if 'Pltm plur' in str(p[1]):
                numer = 'only plur'
            if 'Sgtm sing' in str(p[1]):
                numer = 'only sing'
            if numer in numbers:
                show.append(numbers[numer])
            else:
                show.append('число не определено')

            # определение рода
            gender = p.tag.gender
            genders = {'masc': 'мужской род', 'femn': 'женский род', 'neut': 'средний род', 'ms': 'общего рода'}
            if 'Ms-f' in str(p[1]):
                gender = 'ms'
            if gender in genders:
                show.append(genders[gender])
            else:
                show.append('род не определен')

            # определение одуш/неодуш.
            if 'anim' in str(p[1]):
                show.append('одушевлённое')
            else:
                show.append('неодушевлённое')

        elif show[0] == 'глагол' or show[0] == 'глагол (инфинитив)':
            # определение вида
            if 'perf' in str(p[1]):
                show.append('совершенный вид')
            else:
                show.append('несовершенный вид')

            # определение переходности
            if 'tran' in str(p[1]):
                show.append('переходный')
            else:
                show.append('переходный')

            # определение лица
            if '1per' in str(p[1]):
                show.append('1 лицо')
            elif '2per' in str(p[1]):
                show.append('2 лицо')
            elif '3per' in str(p[1]):
                show.append('3 лицо')
            else:
                show.append('лицо не определено')

            # определение времени
            if 'pres' in str(p[1]):
                show.append('настоящее время')
            elif 'past' in str(p[1]):
                show.append('прошедшее время')
            elif 'futr' in str(p[1]):
                show.append('будущее время')
            else:
                show.append('время не определено')

            # определение наклонения
            if 'indc' in str(p[1]):
                show.append('изъявительное наклонение')
            elif 'impr' in str(p[1]):
                show.append('повелительное наклонение')
            else:
                show.append('наклонение не определено')

            # определение рода
            gender = p.tag.gender
            genders = {'masc': 'мужской род', 'femn': 'женский род', 'neut': 'средний род'}
            if gender in genders:
                show.append(genders[gender])
            else:
                show.append('род не определен')

            # определение возвратности
            if 'Refl' in str(p[1]):
                show.append('возвратный')

            # определение числа
            numer = p.tag.number
            numbers = {'sing': 'единственное число', 'plur': 'множественное число'}
            if numer in numbers:
                show.append(numbers[numer])
            else:
                show.append('число не определено')

            # определение залога
            if 'actv' in str(p[1]):
                show.append('действительный залог')
            elif 'pssv' in str(p[1]):
                show.append('страдательный залог')
            else:
                show.append('залог не определен')

        elif show[0] == 'имя прилагательное':
            # определение разряда
            if 'Qual' in str(p[1]):
                show.append('качественное')
            elif 'Poss' in str(p[1]):
                show.append('притяжательное')
            else:
                show.append('относительное')

            # определение формы (полное или краткое) только у качественных
            if 'Qual' in str(p[1]):
                if p.tag.POS == 'ADJF':
                    show.append('полное')
                else:
                    show.append('краткое')

            # определение степени (положительная, сравнительная или префосх) только у качеств
            if 'Qual' in str(p[1]):
                if 'Cmp2' in str(p[1]) or 'V-ej' in str(p[1]):
                    show.append('сравнительная степень')
                elif 'Supr' in str(p[1]):
                    show.append('превосходная степень')
                else:
                    show.append('положительная степень')

            # определение рода
            gender = p.tag.gender
            genders = {'masc': 'мужской род', 'femn': 'женский род', 'neut': 'средний род'}
            if gender in genders:
                show.append(genders[gender])
            else:
                show.append('род не определен')

            # определение числа
            numer = p.tag.number
            numbers = {'sing': 'единственное число', 'plur': 'множественное число'}
            if numer in numbers:
                show.append(numbers[numer])
            else:
                show.append('число не определено')

            # определение падежа только у полных
            if p.tag.POS == 'ADJF':
                padezh = p.tag.case
                cases = {'nomn': 'именительный падеж', 'gent': 'родительный падеж', 'datv': 'дательный падеж',
                         'accs': 'винительный падеж', 'ablt': 'творительный падеж', 'loct': 'предложный падеж',
                         'voct': 'звательный падеж'}
                if padezh in cases:
                    show.append(cases[padezh])
                else:
                    show.append('падеж не определён')
        k = len(show)
        if ' 'in word or len([i for i in word if i in '`~1234567890!@#$%^&*()_ -+=\|]}[{;:"/?.><,' or i == "'"]) != 0:
            self.label_morph1.setText('Введи текст без точек, запятых и других символов!')
        else:
            if k == 1:
                self.label_morph1.setText('{}'.format(show[0]))
            elif k == 2:
                self.label_morph1.setText('{}'.format(show[0]))
                self.label_morph2.setText('{}'.format(show[1]))
            elif k == 3:
                self.label_morph1.setText('{}'.format(show[0]))
                self.label_morph2.setText('{}'.format(show[1]))
                self.label_morph3.setText('{}'.format(show[2]))
            elif k == 4:
                self.label_morph1.setText('{}'.format(show[0]))
                self.label_morph2.setText('{}'.format(show[1]))
                self.label_morph3.setText('{}'.format(show[2]))
                self.label_morph4.setText('{}'.format(show[3]))
            elif k == 5:
                self.label_morph1.setText('{}'.format(show[0]))
                self.label_morph2.setText('{}'.format(show[1]))
                self.label_morph3.setText('{}'.format(show[2]))
                self.label_morph4.setText('{}'.format(show[3]))
                self.label_morph5.setText('{}'.format(show[4]))
            elif k == 6:
                self.label_morph1.setText('{}'.format(show[0]))
                self.label_morph2.setText('{}'.format(show[1]))
                self.label_morph3.setText('{}'.format(show[2]))
                self.label_morph4.setText('{}'.format(show[3]))
                self.label_morph5.setText('{}'.format(show[4]))
                self.label_morph6.setText('{}'.format(show[5]))
            elif k == 7:
                self.label_morph1.setText('{}'.format(show[0]))
                self.label_morph2.setText('{}'.format(show[1]))
                self.label_morph3.setText('{}'.format(show[2]))
                self.label_morph4.setText('{}'.format(show[3]))
                self.label_morph5.setText('{}'.format(show[4]))
                self.label_morph6.setText('{}'.format(show[5]))
                self.label_morph7.setText('{}'.format(show[6]))
            elif k == 8:
                self.label_morph1.setText('{}'.format(show[0]))
                self.label_morph2.setText('{}'.format(show[1]))
                self.label_morph3.setText('{}'.format(show[2]))
                self.label_morph4.setText('{}'.format(show[3]))
                self.label_morph5.setText('{}'.format(show[4]))
                self.label_morph6.setText('{}'.format(show[5]))
                self.label_morph7.setText('{}'.format(show[6]))
                self.label_morph8.setText('{}'.format(show[7]))
            elif k == 9:
                self.label_morph1.setText('{}'.format(show[0]))
                self.label_morph2.setText('{}'.format(show[1]))
                self.label_morph3.setText('{}'.format(show[2]))
                self.label_morph4.setText('{}'.format(show[3]))
                self.label_morph5.setText('{}'.format(show[4]))
                self.label_morph6.setText('{}'.format(show[5]))
                self.label_morph7.setText('{}'.format(show[6]))
                self.label_morph8.setText('{}'.format(show[7]))
                self.label_morph9.setText('{}'.format(show[8]))
            elif k == 10:
                self.label_morph1.setText('{}'.format(show[0]))
                self.label_morph2.setText('{}'.format(show[1]))
                self.label_morph3.setText('{}'.format(show[2]))
                self.label_morph4.setText('{}'.format(show[3]))
                self.label_morph5.setText('{}'.format(show[4]))
                self.label_morph6.setText('{}'.format(show[5]))
                self.label_morph7.setText('{}'.format(show[6]))
                self.label_morph8.setText('{}'.format(show[7]))
                self.label_morph9.setText('{}'.format(show[8]))
                self.label_morph10.setText('{}'.format(show[9]))

    def phonetics(self):
        ph = {
            "а": "гласный",
            "б": "согласный, звонкий, парный [п], твёрдый, парный [б']",
            "б'": "согласный, звонкий, парный [п'], мягкий, парный [б]",
            "в": "согласный, звонкий, парный [ф], твёрдый, парный [в']",
            "в'": "согласный, звонкий, парный [ф'], мягкий, парный [в]",
            "г": "согласный, звонкий, парный [к], твёрдый, парный [г']",
            "г'": "согласный, звонкий, парный [к'], мягкий, парный [г]",
            "д": "согласный, звонкий, парный [т], твёрдый, парный [д']",
            "д'": "согласный, звонкий, парный [т'], мягкий, парный [д]",
            "ж": "согласный, звонкий, парный [ш], твёрдый, непарный",
            "з": "согласный, звонкий, парный [с], твёрдый, парный [з']",
            "з'": "согласный, звонкий, парный [с'], мягкий, парный [з]",
            "и": "гласный",
            "й'": "согласный, сонорный, непарный, мягкий, непарный",
            "к": "согласный, глухой, парный [г], твёрдый, парный [к']",
            "к'": "согласный, глухой, парный [г'], мягкий, парный [к]",
            "л": "согласный, сонорный, непарный, твёрдый, парный [л']",
            "л'": "согласный, сонорный, непарный, мягкий, парный [л]",
            "м": "согласный, сонорный, непарный, твёрдый, парный [м']",
            "м'": "согласный, сонорный, непарный, мягкий, парный [м]",
            "н": "согласный, сонорный, непарный, твёрдый, парный [н']",
            "н'": "согласный, сонорный, непарный, мягкий, парный [н]",
            "о": "гласный",
            "п": "согласный, глухой, парный [б], твёрдый, парный [п']",
            "п'": "согласный, глухой, парный [б'], мягкий, парный [п]",
            "р": "согласный, сонорный, непарный, твёрдый, парный [р']",
            "р'": "согласный, сонорный, непарный, мягкий, парный [р]",
            "с": "согласный, глухой, парный [з], твёрдый, парный [с']",
            "с'": "согласный, глухой, парный [з'], мягкий, парный [с]",
            "т": "согласный, глухой, парный [д], твёрдый, парный [т']",
            "т'": "согласный, глухой, парный [д'], мягкий, парный [т]",
            "у": "гласный",
            "ф": "согласный, глухой, парный [в], твёрдый, парный [ф']",
            "ф'": "согласный, глухой, парный [в'], мягкий, парный [ф]",
            "х": "согласный, глухой, непарный, твёрдый, парный [х']",
            "х'": "согласный, глухой, непарный, мягкий, парный [х]",
            "ц": "согласный, глухой, непарный, твёрдый, непарный",
            "ч'": "согласный, глухой, непарный, мягкий, непарный",
            "ш": "согласный, глухой, парный [ж], твёрдый, непарный",
            "щ'": "согласный, глухой, непарный, мягкий, непарный",
            "ы": "гласный",
            "э": "гласный"
            }

        word = self.word_input.text()
        word = word.lower().strip()

        d = {
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

        trnscrpt = ''
        for i in range(len(word)):
            if word[i].isalpha() == False:
                trnscrpt = '['
                break
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

        w = trnscrpt

        sounds = []
        for i in range(len(w)):
            if w[i] == "'":
                sounds.append(w[i - 1] + w[i])
        for i in w:
            if i.isalpha() == True and i + "'" not in sounds:
                sounds.append(i)

        sounds = sorted(list(set(sounds)))
        n = len(sounds)

        if n == 1:
            if sounds[0] in ph:
                self.label_sounds1.setText('Звук [{}]: {}'.format(sounds[0], ph[sounds[0]]))
            else:
                self.label_sounds1.setText('Звук {}: {}'.format(sounds[0], 'не определён'))
        elif n == 2:
            if sounds[0] in ph:
                self.label_sounds1.setText('Звук [{}]: {}'.format(sounds[0], ph[sounds[0]]))
            else:
                self.label_sounds1.setText('Звук {}: {}'.format(sounds[0], 'не определён'))
            if sounds[1] in ph:
                self.label_sounds2.setText('Звук [{}]: {}'.format(sounds[1], ph[sounds[1]]))
            else:
                self.label_sounds2.setText('Звук {}: {}'.format(sounds[1], 'не определён'))
        elif n == 3:
            if sounds[0] in ph:
                self.label_sounds1.setText('Звук [{}]: {}'.format(sounds[0], ph[sounds[0]]))
            else:
                self.label_sounds1.setText('Звук {}: {}'.format(sounds[0], 'не определён'))
            if sounds[1] in ph:
                self.label_sounds2.setText('Звук [{}]: {}'.format(sounds[1], ph[sounds[1]]))
            else:
                self.label_sounds2.setText('Звук {}: {}'.format(sounds[1], 'не определён'))
            if sounds[2] in ph:
                self.label_sounds3.setText('Звук [{}]: {}'.format(sounds[2], ph[sounds[2]]))
            else:
                self.label_sounds3.setText('Звук {}: {}'.format(sounds[2], 'не определён'))
        elif n == 4:
            if sounds[0] in ph:
                self.label_sounds1.setText('Звук [{}]: {}'.format(sounds[0], ph[sounds[0]]))
            else:
                self.label_sounds1.setText('Звук {}: {}'.format(sounds[0], 'не определён'))
            if sounds[1] in ph:
                self.label_sounds2.setText('Звук [{}]: {}'.format(sounds[1], ph[sounds[1]]))
            else:
                self.label_sounds2.setText('Звук {}: {}'.format(sounds[1], 'не определён'))
            if sounds[2] in ph:
                self.label_sounds3.setText('Звук [{}]: {}'.format(sounds[2], ph[sounds[2]]))
            else:
                self.label_sounds3.setText('Звук {}: {}'.format(sounds[2], 'не определён'))
            if sounds[3] in ph:
                self.label_sounds4.setText('Звук [{}]: {}'.format(sounds[3], ph[sounds[3]]))
            else:
                self.label_sounds4.setText('Звук {}: {}'.format(sounds[3], 'не определён'))
        elif n == 5:
            if sounds[0] in ph:
                self.label_sounds1.setText('Звук [{}]: {}'.format(sounds[0], ph[sounds[0]]))
            else:
                self.label_sounds1.setText('Звук {}: {}'.format(sounds[0], 'не определён'))
            if sounds[1] in ph:
                self.label_sounds2.setText('Звук [{}]: {}'.format(sounds[1], ph[sounds[1]]))
            else:
                self.label_sounds2.setText('Звук {}: {}'.format(sounds[1], 'не определён'))
            if sounds[2] in ph:
                self.label_sounds3.setText('Звук [{}]: {}'.format(sounds[2], ph[sounds[2]]))
            else:
                self.label_sounds3.setText('Звук {}: {}'.format(sounds[2], 'не определён'))
            if sounds[3] in ph:
                self.label_sounds4.setText('Звук [{}]: {}'.format(sounds[3], ph[sounds[3]]))
            else:
                self.label_sounds4.setText('Звук {}: {}'.format(sounds[3], 'не определён'))
            if sounds[4] in ph:
                self.label_sounds5.setText('Звук [{}]: {}'.format(sounds[4], ph[sounds[4]]))
            else:
                self.label_sounds5.setText('Звук {}: {}'.format(sounds[4], 'не определён'))
        elif n == 6:
            if sounds[0] in ph:
                self.label_sounds1.setText('Звук [{}]: {}'.format(sounds[0], ph[sounds[0]]))
            else:
                self.label_sounds1.setText('Звук {}: {}'.format(sounds[0], 'не определён'))
            if sounds[1] in ph:
                self.label_sounds2.setText('Звук [{}]: {}'.format(sounds[1], ph[sounds[1]]))
            else:
                self.label_sounds2.setText('Звук {}: {}'.format(sounds[1], 'не определён'))
            if sounds[2] in ph:
                self.label_sounds3.setText('Звук [{}]: {}'.format(sounds[2], ph[sounds[2]]))
            else:
                self.label_sounds3.setText('Звук {}: {}'.format(sounds[2], 'не определён'))
            if sounds[3] in ph:
                self.label_sounds4.setText('Звук [{}]: {}'.format(sounds[3], ph[sounds[3]]))
            else:
                self.label_sounds4.setText('Звук {}: {}'.format(sounds[3], 'не определён'))
            if sounds[4] in ph:
                self.label_sounds5.setText('Звук [{}]: {}'.format(sounds[4], ph[sounds[4]]))
            else:
                self.label_sounds5.setText('Звук {}: {}'.format(sounds[4], 'не определён'))
            if sounds[5] in ph:
                self.label_sounds6.setText('Звук [{}]: {}'.format(sounds[5], ph[sounds[5]]))
            else:
                self.label_sounds6.setText('Звук {}: {}'.format(sounds[5], 'не определён'))
        elif n == 7:
            if sounds[0] in ph:
                self.label_sounds1.setText('Звук [{}]: {}'.format(sounds[0], ph[sounds[0]]))
            else:
                self.label_sounds1.setText('Звук {}: {}'.format(sounds[0], 'не определён'))
            if sounds[1] in ph:
                self.label_sounds2.setText('Звук [{}]: {}'.format(sounds[1], ph[sounds[1]]))
            else:
                self.label_sounds2.setText('Звук {}: {}'.format(sounds[1], 'не определён'))
            if sounds[2] in ph:
                self.label_sounds3.setText('Звук [{}]: {}'.format(sounds[2], ph[sounds[2]]))
            else:
                self.label_sounds3.setText('Звук {}: {}'.format(sounds[2], 'не определён'))
            if sounds[3] in ph:
                self.label_sounds4.setText('Звук [{}]: {}'.format(sounds[3], ph[sounds[3]]))
            else:
                self.label_sounds4.setText('Звук {}: {}'.format(sounds[3], 'не определён'))
            if sounds[4] in ph:
                self.label_sounds5.setText('Звук [{}]: {}'.format(sounds[4], ph[sounds[4]]))
            else:
                self.label_sounds5.setText('Звук {}: {}'.format(sounds[4], 'не определён'))
            if sounds[5] in ph:
                self.label_sounds6.setText('Звук [{}]: {}'.format(sounds[5], ph[sounds[5]]))
            else:
                self.label_sounds6.setText('Звук {}: {}'.format(sounds[5], 'не определён'))
            if sounds[6] in ph:
                self.label_sounds7.setText('Звук [{}]: {}'.format(sounds[6], ph[sounds[6]]))
            else:
                self.label_sounds7.setText('Звук {}: {}'.format(sounds[6], 'не определён'))
        elif n == 8:
            if sounds[0] in ph:
                self.label_sounds1.setText('Звук [{}]: {}'.format(sounds[0], ph[sounds[0]]))
            else:
                self.label_sounds1.setText('Звук {}: {}'.format(sounds[0], 'не определён'))
            if sounds[1] in ph:
                self.label_sounds2.setText('Звук [{}]: {}'.format(sounds[1], ph[sounds[1]]))
            else:
                self.label_sounds2.setText('Звук {}: {}'.format(sounds[1], 'не определён'))
            if sounds[2] in ph:
                self.label_sounds3.setText('Звук [{}]: {}'.format(sounds[2], ph[sounds[2]]))
            else:
                self.label_sounds3.setText('Звук {}: {}'.format(sounds[2], 'не определён'))
            if sounds[3] in ph:
                self.label_sounds4.setText('Звук [{}]: {}'.format(sounds[3], ph[sounds[3]]))
            else:
                self.label_sounds4.setText('Звук {}: {}'.format(sounds[3], 'не определён'))
            if sounds[4] in ph:
                self.label_sounds5.setText('Звук [{}]: {}'.format(sounds[4], ph[sounds[4]]))
            else:
                self.label_sounds5.setText('Звук {}: {}'.format(sounds[4], 'не определён'))
            if sounds[5] in ph:
                self.label_sounds6.setText('Звук [{}]: {}'.format(sounds[5], ph[sounds[5]]))
            else:
                self.label_sounds6.setText('Звук {}: {}'.format(sounds[5], 'не определён'))
            if sounds[6] in ph:
                self.label_sounds7.setText('Звук [{}]: {}'.format(sounds[6], ph[sounds[6]]))
            else:
                self.label_sounds7.setText('Звук {}: {}'.format(sounds[6], 'не определён'))
            if sounds[7] in ph:
                self.label_sounds8.setText('Звук [{}]: {}'.format(sounds[7], ph[sounds[7]]))
            else:
                self.label_sounds8.setText('Звук {}: {}'.format(sounds[7], 'не определён'))
        elif n == 9:
            if sounds[0] in ph:
                self.label_sounds1.setText('Звук [{}]: {}'.format(sounds[0], ph[sounds[0]]))
            else:
                self.label_sounds1.setText('Звук {}: {}'.format(sounds[0], 'не определён'))
            if sounds[1] in ph:
                self.label_sounds2.setText('Звук [{}]: {}'.format(sounds[1], ph[sounds[1]]))
            else:
                self.label_sounds2.setText('Звук {}: {}'.format(sounds[1], 'не определён'))
            if sounds[2] in ph:
                self.label_sounds3.setText('Звук [{}]: {}'.format(sounds[2], ph[sounds[2]]))
            else:
                self.label_sounds3.setText('Звук {}: {}'.format(sounds[2], 'не определён'))
            if sounds[3] in ph:
                self.label_sounds4.setText('Звук [{}]: {}'.format(sounds[3], ph[sounds[3]]))
            else:
                self.label_sounds4.setText('Звук {}: {}'.format(sounds[3], 'не определён'))
            if sounds[4] in ph:
                self.label_sounds5.setText('Звук [{}]: {}'.format(sounds[4], ph[sounds[4]]))
            else:
                self.label_sounds5.setText('Звук {}: {}'.format(sounds[4], 'не определён'))
            if sounds[5] in ph:
                self.label_sounds6.setText('Звук [{}]: {}'.format(sounds[5], ph[sounds[5]]))
            else:
                self.label_sounds6.setText('Звук {}: {}'.format(sounds[5], 'не определён'))
            if sounds[6] in ph:
                self.label_sounds7.setText('Звук [{}]: {}'.format(sounds[6], ph[sounds[6]]))
            else:
                self.label_sounds7.setText('Звук {}: {}'.format(sounds[6], 'не определён'))
            if sounds[7] in ph:
                self.label_sounds8.setText('Звук [{}]: {}'.format(sounds[7], ph[sounds[7]]))
            else:
                self.label_sounds8.setText('Звук {}: {}'.format(sounds[7], 'не определён'))
            if sounds[8] in ph:
                self.label_sounds9.setText('Звук [{}]: {}'.format(sounds[8], ph[sounds[8]]))
            else:
                self.label_sounds9.setText('Звук {}: {}'.format(sounds[8], 'не определён'))
        elif n == 10:
            if sounds[0] in ph:
                self.label_sounds1.setText('Звук [{}]: {}'.format(sounds[0], ph[sounds[0]]))
            else:
                self.label_sounds1.setText('Звук {}: {}'.format(sounds[0], 'не определён'))
            if sounds[1] in ph:
                self.label_sounds2.setText('Звук [{}]: {}'.format(sounds[1], ph[sounds[1]]))
            else:
                self.label_sounds2.setText('Звук {}: {}'.format(sounds[1], 'не определён'))
            if sounds[2] in ph:
                self.label_sounds3.setText('Звук [{}]: {}'.format(sounds[2], ph[sounds[2]]))
            else:
                self.label_sounds3.setText('Звук {}: {}'.format(sounds[2], 'не определён'))
            if sounds[3] in ph:
                self.label_sounds4.setText('Звук [{}]: {}'.format(sounds[3], ph[sounds[3]]))
            else:
                self.label_sounds4.setText('Звук {}: {}'.format(sounds[3], 'не определён'))
            if sounds[4] in ph:
                self.label_sounds5.setText('Звук [{}]: {}'.format(sounds[4], ph[sounds[4]]))
            else:
                self.label_sounds5.setText('Звук {}: {}'.format(sounds[4], 'не определён'))
            if sounds[5] in ph:
                self.label_sounds6.setText('Звук [{}]: {}'.format(sounds[5], ph[sounds[5]]))
            else:
                self.label_sounds6.setText('Звук {}: {}'.format(sounds[5], 'не определён'))
            if sounds[6] in ph:
                self.label_sounds7.setText('Звук [{}]: {}'.format(sounds[6], ph[sounds[6]]))
            else:
                self.label_sounds7.setText('Звук {}: {}'.format(sounds[6], 'не определён'))
            if sounds[7] in ph:
                self.label_sounds8.setText('Звук [{}]: {}'.format(sounds[7], ph[sounds[7]]))
            else:
                self.label_sounds8.setText('Звук {}: {}'.format(sounds[7], 'не определён'))
            if sounds[8] in ph:
                self.label_sounds9.setText('Звук [{}]: {}'.format(sounds[8], ph[sounds[8]]))
            else:
                self.label_sounds9.setText('Звук {}: {}'.format(sounds[8], 'не определён'))
            if sounds[9] in ph:
                self.label_sounds10.setText('Звук [{}]: {}'.format(sounds[9], ph[sounds[9]]))
            else:
                self.label_sounds10.setText('Звук {}: {}'.format(sounds[9], 'не определён'))
        elif n == 11:
            if sounds[0] in ph:
                self.label_sounds1.setText('Звук [{}]: {}'.format(sounds[0], ph[sounds[0]]))
            else:
                self.label_sounds1.setText('Звук {}: {}'.format(sounds[0], 'не определён'))
            if sounds[1] in ph:
                self.label_sounds2.setText('Звук [{}]: {}'.format(sounds[1], ph[sounds[1]]))
            else:
                self.label_sounds2.setText('Звук {}: {}'.format(sounds[1], 'не определён'))
            if sounds[2] in ph:
                self.label_sounds3.setText('Звук [{}]: {}'.format(sounds[2], ph[sounds[2]]))
            else:
                self.label_sounds3.setText('Звук {}: {}'.format(sounds[2], 'не определён'))
            if sounds[3] in ph:
                self.label_sounds4.setText('Звук [{}]: {}'.format(sounds[3], ph[sounds[3]]))
            else:
                self.label_sounds4.setText('Звук {}: {}'.format(sounds[3], 'не определён'))
            if sounds[4] in ph:
                self.label_sounds5.setText('Звук [{}]: {}'.format(sounds[4], ph[sounds[4]]))
            else:
                self.label_sounds5.setText('Звук {}: {}'.format(sounds[4], 'не определён'))
            if sounds[5] in ph:
                self.label_sounds6.setText('Звук [{}]: {}'.format(sounds[5], ph[sounds[5]]))
            else:
                self.label_sounds6.setText('Звук {}: {}'.format(sounds[5], 'не определён'))
            if sounds[6] in ph:
                self.label_sounds7.setText('Звук [{}]: {}'.format(sounds[6], ph[sounds[6]]))
            else:
                self.label_sounds7.setText('Звук {}: {}'.format(sounds[6], 'не определён'))
            if sounds[7] in ph:
                self.label_sounds8.setText('Звук [{}]: {}'.format(sounds[7], ph[sounds[7]]))
            else:
                self.label_sounds8.setText('Звук {}: {}'.format(sounds[7], 'не определён'))
            if sounds[8] in ph:
                self.label_sounds9.setText('Звук [{}]: {}'.format(sounds[8], ph[sounds[8]]))
            else:
                self.label_sounds9.setText('Звук {}: {}'.format(sounds[8], 'не определён'))
            if sounds[9] in ph:
                self.label_sounds10.setText('Звук [{}]: {}'.format(sounds[9], ph[sounds[9]]))
            else:
                self.label_sounds10.setText('Звук {}: {}'.format(sounds[9], 'не определён'))
            if sounds[10] in ph:
                self.label_sounds11.setText('Звук [{}]: {}'.format(sounds[10], ph[sounds[10]]))
            else:
                self.label_sounds11.setText('Звук {}: {}'.format(sounds[10], 'не определён'))
        elif n > 11:
            self.label_sounds1.setText('Слишком много звуков!')



def main():
    app = QApplication(sys.argv)
    entry = Beginning()
    entry.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()