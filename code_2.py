from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber
from PyQt5.QtGui import QPixmap
from PyQt5.Qt import QFont
import sys
import pymorphy2
import random
import pyttsx3

class Beginning(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 50, 1800, 950)
        self.setWindowTitle('ЗВУК И СЛОВО')
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
        self.butt.setStyleSheet("background-color: #EEE8AA; \
        color: #008080; font-family: Arial; font-style: normal; \
        font-size: 19pt; font-weight: bold")
        self.butt.resize(500, 150)
        self.butt.move(700, 450)
        self.butt.clicked.connect(self.destroy_beginning)

        self.butt_2 = QPushButton('НАЧАТЬ!\n(версия для слабовидящих)', self)
        self.butt_2.setStyleSheet("background-color: #EEE8AA; \
        color: #008080; font-family: Arial; font-style: normal; \
        font-size: 21pt; font-weight: bold")
        self.butt_2.resize(500, 200)
        self.butt_2.move(700, 650)
        self.butt_2.clicked.connect(self.destroy_beginning_to_person_with_disabilities)

    def destroy_beginning(self):
        self.close()
        self.MainWindow = Window()
        self.MainWindow.show()

    def destroy_beginning_to_person_with_disabilities(self):
        self.close()
        self.MainWindow = Window_for_person_with_disabilities()
        self.MainWindow.show()


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 50, 1900, 1000)
        self.setWindowTitle('ЗВУК И СЛОВО')
        self.setStyleSheet("background-color: #7FFFD4; \
        color: #007A7A; font-family: Arial; \
        font-style: normal; font-size: 16pt; font-weight: bold")


class Window_for_person_with_disabilities(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 50, 1900, 1000)
        self.setWindowTitle('ЗВУК И СЛОВО')
        self.setStyleSheet("background-color: #7FFFD4; \
        color: #007A7A; font-family: Arial; \
        font-style: normal; font-size: 31pt; font-weight: bold")

        self.word_label = QLabel(self)
        self.word_label.setText("ВВЕДИ СЛОВО:")
        self.word_label.move(10, 15)

        self.word_input = QLineEdit(self)
        self.word_input.move(420, 10)
        self.word_input.setStyleSheet("background-color: #6DB5DC; color: #324166")
        self.word_input.resize(690, 70)

        self.btn_1 = QPushButton('Нажми сюда, когда введёшь слово', self)
        self.btn_1.resize(915, 70)
        self.btn_1.move(10, 85)
        self.btn_1.setStyleSheet("background-color: #12C6B4; color: #F7F38D")
        self.btn_1.clicked.connect(self.give_info)

        self.btn_2 = QPushButton('▶', self)
        self.btn_2.resize(120, 120)
        self.btn_2.move(935, 85)
        self.btn_2.setStyleSheet("background-color: #DC6DD9; color: #F7F38D; font-size: 100pt")
        self.btn_2.clicked.connect(self.say_word)


        self.label_l = QLineEdit(self)
        self.label_l.setStyleSheet("background-color: #FFC4FA; color: #9C398A")
        self.label_l.setText("Буквы в слове")
        self.label_l.move(1150, 10)
        self.label_l.resize(750, 60)

        self.label_v = QLineEdit(self)
        self.label_v.setStyleSheet("background-color: #FFC4FA; color: #9C398A")
        self.label_v.setText("Гласные в слове")
        self.label_v.move(1150, 70)
        self.label_v.resize(750, 60)

        self.label_c = QLineEdit(self)
        self.label_c.setStyleSheet("background-color: #FFC4FA; color: #9C398A")
        self.label_c.setText("Согласные в слове")
        self.label_c.move(1150, 130)
        self.label_c.resize(750, 60)

        self.label_an = QLineEdit(self)
        self.label_an.setStyleSheet("background-color: #FFC4FA; color: #9C398A")
        self.label_an.setText("Иное")
        self.label_an.move(1150, 190)
        self.label_an.resize(750, 60)

        self.label1 = QLineEdit(self)
        self.label1.setStyleSheet("background-color: #FFC4FA; color: #9C398A")
        self.label1.setText("Транскрипция")
        self.label1.move(1150, 250)
        self.label1.resize(750, 60)


        sound_color = "background-color: #FDE9C3; color: #FCBB43; font-size: 23pt"
        self.word_label_2 = QLabel(self)
        self.word_label_2.setStyleSheet("color: #CD890C")
        self.word_label_2.setText("Фонетический разбор:")
        self.word_label_2.move(10, 170)

        self.label_sounds1 = QLineEdit(self)
        # self.label_sounds1.setStyleSheet("font-size: 23pt")
        self.label_sounds1.setStyleSheet(sound_color)
        self.label_sounds1.setText("")
        self.label_sounds1.move(10, 235)
        self.label_sounds1.resize(1100, 70)

        self.label_sounds2 = QLineEdit(self)
        self.label_sounds2.setStyleSheet(sound_color)
        self.label_sounds2.setText("")
        self.label_sounds2.move(10, 305)
        self.label_sounds2.resize(1100, 70)

        self.label_sounds3 = QLineEdit(self)
        self.label_sounds3.setStyleSheet(sound_color)
        self.label_sounds3.setText("")
        self.label_sounds3.move(10, 375)
        self.label_sounds3.resize(1100, 70)

        self.label_sounds4 = QLineEdit(self)
        self.label_sounds4.setStyleSheet(sound_color)
        self.label_sounds4.setText("")
        self.label_sounds4.move(10, 445)
        self.label_sounds4.resize(1100, 70)

        self.label_sounds5 = QLineEdit(self)
        self.label_sounds5.setStyleSheet(sound_color)
        self.label_sounds5.setText("")
        self.label_sounds5.move(10, 515)
        self.label_sounds5.resize(1100, 70)

        self.label_sounds6 = QLineEdit(self)
        self.label_sounds6.setStyleSheet(sound_color)
        self.label_sounds6.setText("")
        self.label_sounds6.move(10, 585)
        self.label_sounds6.resize(1100, 70)

        self.label_sounds7 = QLineEdit(self)
        self.label_sounds7.setStyleSheet(sound_color)
        self.label_sounds7.setText("")
        self.label_sounds7.move(10, 655)
        self.label_sounds7.resize(1100, 70)

        self.label_sounds8 = QLineEdit(self)
        self.label_sounds8.setStyleSheet(sound_color)
        self.label_sounds8.setText("")
        self.label_sounds8.move(10, 725)
        self.label_sounds8.resize(1100, 70)

        self.label_sounds9 = QLineEdit(self)
        self.label_sounds9.setStyleSheet(sound_color)
        self.label_sounds9.setText("")
        self.label_sounds9.move(10, 795)
        self.label_sounds9.resize(1100, 70)

        self.label_sounds10 = QLineEdit(self)
        self.label_sounds10.setStyleSheet(sound_color)
        self.label_sounds10.setText("")
        self.label_sounds10.move(10, 865)
        self.label_sounds10.resize(1100, 70)


        morph_color = "background-color: #C5BDF6; color: #753A93"
        self.word_label_3 = QLabel(self)
        self.word_label_3.setStyleSheet("color: #686382")
        self.word_label_3.setText("Морфологический разбор:")
        self.word_label_3.move(1150, 320)

        self.label_morph1 = QLineEdit(self)
        self.label_morph1.setStyleSheet(morph_color)
        self.label_morph1.setText("")
        self.label_morph1.move(1150, 385)
        self.label_morph1.resize(750, 70)

        self.label_morph2 = QLineEdit(self)
        self.label_morph2.setStyleSheet(morph_color)
        self.label_morph2.setText("")
        self.label_morph2.move(1150, 455)
        self.label_morph2.resize(750, 70)

        self.label_morph3 = QLineEdit(self)
        self.label_morph3.setStyleSheet(morph_color)
        self.label_morph3.setText("")
        self.label_morph3.move(1150, 525)
        self.label_morph3.resize(750, 70)

        self.label_morph4 = QLineEdit(self)
        self.label_morph4.setStyleSheet(morph_color)
        self.label_morph4.setText("")
        self.label_morph4.move(1150, 595)
        self.label_morph4.resize(750, 70)

        self.label_morph5 = QLineEdit(self)
        self.label_morph5.setStyleSheet(morph_color)
        self.label_morph5.setText("")
        self.label_morph5.move(1150, 665)
        self.label_morph5.resize(750, 70)

        self.label_morph6 = QLineEdit(self)
        self.label_morph6.setStyleSheet(morph_color)
        self.label_morph6.setText("")
        self.label_morph6.move(1150, 735)
        self.label_morph6.resize(750, 70)

        self.label_morph7 = QLineEdit(self)
        self.label_morph7.setStyleSheet(morph_color)
        self.label_morph7.setText("")
        self.label_morph7.move(1150, 805)
        self.label_morph7.resize(750, 70)

        self.label_morph8 = QLineEdit(self)
        self.label_morph8.setStyleSheet(morph_color)
        self.label_morph8.setText("")
        self.label_morph8.move(1150, 875)
        self.label_morph8.resize(750, 70)




    def say_word(self):
        word = self.word_input.text()
        engine = pyttsx3.init()
        ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
        engine.setProperty('voice', ru_voice_id)
        engine.say(word)
        engine.runAndWait()


    def give_info(self):
        self.label_l.setText("")
        self.label_v.setText("")
        self.label_c.setText("")
        self.label_an.setText("")
        self.label1.setText("")
        self.label_morph1.setText("")
        self.label_morph2.setText("")
        self.label_morph3.setText("")
        self.label_morph4.setText("")
        self.label_morph5.setText("")
        self.label_morph6.setText("")
        self.label_morph7.setText("")
        self.label_morph8.setText("")
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
        word = self.word_input.text().lower().strip()

        if word == '':
            self.label_l.setText("")
            self.label_v.setText("")
            self.label_c.setText("")
            self.label_an.setText("")
            self.label1.setText("")
            self.label_morph1.setText("")
            self.label_morph2.setText("")
            self.label_morph3.setText("")
            self.label_morph4.setText("")
            self.label_morph5.setText("")
            self.label_morph6.setText("")
            self.label_morph7.setText("")
            self.label_morph8.setText("")
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

            color = "background-color: #FFC4FA; color: #9C398A"
            self.label_l.setStyleSheet(color)
            self.label_v.setStyleSheet(color)
            self.label_c.setStyleSheet(color)
            self.label_an.setStyleSheet(color)
            self.label1.setStyleSheet(color)
    
            color_2 = "background-color: #C5BDF6; color: #753A93"
            self.label_morph1.setStyleSheet(color_2)
            self.label_morph2.setStyleSheet(color_2)
            self.label_morph3.setStyleSheet(color_2)
            self.label_morph4.setStyleSheet(color_2)
            self.label_morph5.setStyleSheet(color_2)
            self.label_morph6.setStyleSheet(color_2)
            self.label_morph7.setStyleSheet(color_2)
            self.label_morph8.setStyleSheet(color_2)
            
            color_3 = "background-color: #FDE9C3; color: #FCBB43; font-size: 23pt"
            self.label_sounds1.setStyleSheet(color_3)
            self.label_sounds2.setStyleSheet(color_3)
            self.label_sounds3.setStyleSheet(color_3)
            self.label_sounds4.setStyleSheet(color_3)
            self.label_sounds5.setStyleSheet(color_3)
            self.label_sounds6.setStyleSheet(color_3)
            self.label_sounds7.setStyleSheet(color_3)
            self.label_sounds8.setStyleSheet(color_3)
            self.label_sounds9.setStyleSheet(color_3)
            self.label_sounds10.setStyleSheet(color_3)



        elif len([i for i in word if i in 'qwertyuioplkjhgfdsazxcvbnm']) != 0:
            self.label_l.setText("Это иностранное слово!")
            self.label_v.setText("")
            self.label_c.setText("")
            self.label_an.setText("")
            self.label1.setText("")
            self.label_morph1.setText("Это иностранное слово!")
            self.label_morph2.setText("")
            self.label_morph3.setText("")
            self.label_morph4.setText("")
            self.label_morph5.setText("")
            self.label_morph6.setText("")
            self.label_morph7.setText("")
            self.label_morph8.setText("")
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

            color = "background-color: #E69898; color: #8B0000"
            self.label_l.setStyleSheet(color)
            self.label_v.setStyleSheet(color)
            self.label_c.setStyleSheet(color)
            self.label_an.setStyleSheet(color)
            self.label1.setStyleSheet(color)
            self.label_morph1.setStyleSheet(color)
            self.label_morph2.setStyleSheet(color)
            self.label_morph3.setStyleSheet(color)
            self.label_morph4.setStyleSheet(color)
            self.label_morph5.setStyleSheet(color)
            self.label_morph6.setStyleSheet(color)
            self.label_morph7.setStyleSheet(color)
            self.label_morph8.setStyleSheet(color)
            self.label_sounds1.setStyleSheet(color)
            self.label_sounds2.setStyleSheet(color)
            self.label_sounds3.setStyleSheet(color)
            self.label_sounds4.setStyleSheet(color)
            self.label_sounds5.setStyleSheet(color)
            self.label_sounds6.setStyleSheet(color)
            self.label_sounds7.setStyleSheet(color)
            self.label_sounds8.setStyleSheet(color)
            self.label_sounds9.setStyleSheet(color)
            self.label_sounds10.setStyleSheet(color)
            

        elif len([i for i in word if i.isalpha() == False]) != 0:
            self.label1.setText("")
            self.label_morph1.setText("Введи тест без символов!")
            self.label_morph2.setText("")
            self.label_morph3.setText("")
            self.label_morph4.setText("")
            self.label_morph5.setText("")
            self.label_morph6.setText("")
            self.label_morph7.setText("")
            self.label_morph8.setText("")
            self.label_sounds1.setText('Введи тест без символов!')
            self.label_sounds2.setText('')
            self.label_sounds3.setText('')
            self.label_sounds4.setText('')
            self.label_sounds5.setText('')
            self.label_sounds6.setText('')
            self.label_sounds7.setText('')
            self.label_sounds8.setText('')
            self.label_sounds9.setText('')
            self.label_sounds10.setText('')

            color = "background-color: #E69898; color: #8B0000"
            self.label1.setStyleSheet(color)
            self.label_morph1.setStyleSheet(color)
            self.label_morph2.setStyleSheet(color)
            self.label_morph3.setStyleSheet(color)
            self.label_morph4.setStyleSheet(color)
            self.label_morph5.setStyleSheet(color)
            self.label_morph6.setStyleSheet(color)
            self.label_morph7.setStyleSheet(color)
            self.label_morph8.setStyleSheet(color)
            self.label_sounds1.setStyleSheet(color)
            self.label_sounds2.setStyleSheet(color)
            self.label_sounds3.setStyleSheet(color)
            self.label_sounds4.setStyleSheet(color)
            self.label_sounds5.setStyleSheet(color)
            self.label_sounds6.setStyleSheet(color)
            self.label_sounds7.setStyleSheet(color)
            self.label_sounds8.setStyleSheet(color)
            self.label_sounds9.setStyleSheet(color)
            self.label_sounds10.setStyleSheet(color)
            
            color_2 = "background-color: #FFC4FA; color: #9C398A"
            self.label_l.setStyleSheet(color_2)
            self.label_v.setStyleSheet(color_2)
            self.label_c.setStyleSheet(color_2)
            self.label_an.setStyleSheet(color_2)

            letters = [chr(i) for i in range(ord('а'), ord('я') + 1)]
            vowels = ['а', 'у', 'о', 'е', 'и', 'я', 'ю', 'ё', 'э', 'ы']
            cons = list('йцкнгшщзхждлрпвфчмстб')

            l = set([i for i in word if i in letters])
            v = set([i for i in word if i in vowels])
            c = set([i for i in word if i in cons])
            an = set([i for i in word if i \
                        not in c and i not in v and i != ' '])

            if len(l) != 0:
                self.label_l.setText('{}'.format(', '.join(sorted([i for i in l]))))
            else:
                self.label_l.setText('Букв нет')
            if len(v) != 0:
                self.label_v.setText('{}'.format(', '.join(sorted([i for i in v]))))
            else:
                self.label_v.setText('Гласных нет')
            if len(c) != 0:
                self.label_c.setText('{}'.format(', '.join(sorted([i for i in c]))))
            else:
                self.label_c.setText('Согласных нет')
            if len(an) != 0:
                self.label_an.setText('Иные символы: {}'.format(', '.join([i for i in an])))
            else:
                self.label_an.setText('Иных символов нет')

        elif len([i for i in word if i in 'йцукенгшщзхъэждлорпавыфячсмитьбю']) == len(word):
            color = "background-color: #FFC4FA; color: #9C398A"
            self.label_l.setStyleSheet(color)
            self.label_v.setStyleSheet(color)
            self.label_c.setStyleSheet(color)
            self.label_an.setStyleSheet(color)
            self.label1.setStyleSheet(color)
            
            color_2 = "background-color: #C5BDF6; color: #753A93"
            self.label_morph1.setStyleSheet(color_2)
            self.label_morph2.setStyleSheet(color_2)
            self.label_morph3.setStyleSheet(color_2)
            self.label_morph4.setStyleSheet(color_2)
            self.label_morph5.setStyleSheet(color_2)
            self.label_morph6.setStyleSheet(color_2)
            self.label_morph7.setStyleSheet(color_2)
            self.label_morph8.setStyleSheet(color_2)
            
            color_3 = "background-color: #FDE9C3; color: #CD890C; font-size: 22pt"
            self.label_sounds1.setStyleSheet(color_3)
            self.label_sounds2.setStyleSheet(color_3)
            self.label_sounds3.setStyleSheet(color_3)
            self.label_sounds4.setStyleSheet(color_3)
            self.label_sounds5.setStyleSheet(color_3)
            self.label_sounds6.setStyleSheet(color_3)
            self.label_sounds7.setStyleSheet(color_3)
            self.label_sounds8.setStyleSheet(color_3)
            self.label_sounds9.setStyleSheet(color_3)
            self.label_sounds10.setStyleSheet(color_3)

            # РАЗБОР ПО БУКВАМ И СИМВОЛАМ
            letters = [chr(i) for i in range(ord('а'), ord('я') + 1)]
            vowels = ['а', 'у', 'о', 'е', 'и', 'я', 'ю', 'ё', 'э', 'ы']
            cons = list('йцкнгшщзхждлрпвфчмстб')
    
            l = set([i for i in word if i in letters])
            v = set([i for i in word if i in vowels])
            c = set([i for i in word if i in cons])
            an = set([i for i in word if i \
                        not in c and i not in v and i != ' '])

            if len(l) != 0:
                self.label_l.setText('{}'.format(', '.join(sorted([i for i in l]))))
            else:
                self.label_l.setText('Букв нет')
            if len(v) != 0:
                self.label_v.setText('{}'.format(', '.join(sorted([i for i in v]))))
            else:
                self.label_v.setText('Гласных нет')
            if len(c) != 0:
                self.label_c.setText('{}'.format(', '.join(sorted([i for i in c]))))
            else:
                self.label_c.setText('Согласных нет')
            if len(an) != 0:
                self.label_an.setText('Иные символы: {}'.format(', '.join([i for i in an])))
            else:
                self.label_an.setText('Иных символов нет')



            # ТРАНСКРИПЦИЯ
            transcrp_dict ={
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
                if word[i] in transcrp_dict:
                    w = word[i]
    
                    if w in vowels:
                        if w in 'уэоаыи':
                            trnscrpt += w
                        elif w in 'ёеяю':
                            if i == 0:
                                trnscrpt += transcrp_dict[w][1]
                            else:
                                if word[i - 1] in vowels or word[i - 1] in smth:
                                    trnscrpt += transcrp_dict[w][1]
                                else:
                                    trnscrpt += transcrp_dict[w][0]
    
                    if w in consonants:
                        if w in 'йцшщжч':
                            trnscrpt += transcrp_dict[w]
                        else:
                            if i != len(word)-1 and word[i + 1] in 'ёеяиью':
                                trnscrpt += transcrp_dict[w][1]
                            else:
                                trnscrpt += transcrp_dict[w][0]
                    if w.isalpha() == False:
                        trnscrpt += w

            trnscrpt += ']'
            if trnscrpt == '[]':
                trnscrpt = ''

            self.label1.setText(trnscrpt)



            # МОРФОЛОГИЧЕСКИЕ ПРИЗНАКИ
            morph = pymorphy2.MorphAnalyzer()
            show = []
            p = morph.parse(word)[0]
            poses = {'VERB': 'глагол', 'NOUN': 'имя существительное',
                     'ADJF': 'имя прилагательное',
                     'ADJS': 'имя прилагательное', 'INFN': 'глагол (инфинитив)',
                     'PRTF': 'причастие (полное)', 'PRTS': 'причастие (краткое)',
                     'GRND': 'деепричастие', 'NUMR': 'числительное',
                     'ADVB': 'наречие', 'NPRO': 'местоимение', 'PREP': 'предлог',
                     'CONJ': 'союз', 'PRCL': 'частица', 'INTJ': 'междометие'}
            if p.tag.POS in poses:
                show.append(poses[p.tag.POS])
            else:
                return 'не определено'
    
            if show[0] == 'имя существительное':
                # определение падежа
                padezh = p.tag.case
                cases = {
                    'nomn': 'именительный падеж',
                         'gent': 'родительный падеж',
                         'datv': 'дательный падеж',
                         'accs': 'винительный падеж',
                         'ablt': 'творительный падеж',
                         'loct': 'предложный падеж',
                         'voct': 'звательный падеж'
                         }
                if padezh in cases:
                    show.append(cases[padezh])
                else:
                    show.append('падеж не определён')
    
                # определение числа
                numer = p.tag.number
                numbers = {
                    'sing': 'единственное число',
                    'plur': 'множественное число',
                    'only sing': 'только единственное число',
                    'only plur': 'только множественное число'
                }
    
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
            elif k >= 8:
                self.label_morph1.setText('{}'.format(show[0]))
                self.label_morph2.setText('{}'.format(show[1]))
                self.label_morph3.setText('{}'.format(show[2]))
                self.label_morph4.setText('{}'.format(show[3]))
                self.label_morph5.setText('{}'.format(show[4]))
                self.label_morph6.setText('{}'.format(show[5]))
                self.label_morph7.setText('{}'.format(show[6]))
                self.label_morph8.setText('{}'.format(show[7]))



            # ФOНЕТИЧЕСКИЙ РАЗБОР
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
                    self.label_sounds1.setText('[{}]: {}'.format(sounds[0], ph[sounds[0]]))
                else:
                    self.label_sounds1.setText('{}: {}'.format(sounds[0], 'не определён'))
            elif n == 2:
                if sounds[0] in ph:
                    self.label_sounds1.setText('[{}]: {}'.format(sounds[0], ph[sounds[0]]))
                else:
                    self.label_sounds1.setText('{}: {}'.format(sounds[0], 'не определён'))
                if sounds[1] in ph:
                    self.label_sounds2.setText('[{}]: {}'.format(sounds[1], ph[sounds[1]]))
                else:
                    self.label_sounds2.setText('{}: {}'.format(sounds[1], 'не определён'))
            elif n == 3:
                if sounds[0] in ph:
                    self.label_sounds1.setText('[{}]: {}'.format(sounds[0], ph[sounds[0]]))
                else:
                    self.label_sounds1.setText('{}: {}'.format(sounds[0], 'не определён'))
                if sounds[1] in ph:
                    self.label_sounds2.setText('[{}]: {}'.format(sounds[1], ph[sounds[1]]))
                else:
                    self.label_sounds2.setText('{}: {}'.format(sounds[1], 'не определён'))
                if sounds[2] in ph:
                    self.label_sounds3.setText('[{}]: {}'.format(sounds[2], ph[sounds[2]]))
                else:
                    self.label_sounds3.setText('{}: {}'.format(sounds[2], 'не определён'))
            elif n == 4:
                if sounds[0] in ph:
                    self.label_sounds1.setText('[{}]: {}'.format(sounds[0], ph[sounds[0]]))
                else:
                    self.label_sounds1.setText('{}: {}'.format(sounds[0], 'не определён'))
                if sounds[1] in ph:
                    self.label_sounds2.setText('[{}]: {}'.format(sounds[1], ph[sounds[1]]))
                else:
                    self.label_sounds2.setText('{}: {}'.format(sounds[1], 'не определён'))
                if sounds[2] in ph:
                    self.label_sounds3.setText('[{}]: {}'.format(sounds[2], ph[sounds[2]]))
                else:
                    self.label_sounds3.setText('{}: {}'.format(sounds[2], 'не определён'))
                if sounds[3] in ph:
                    self.label_sounds4.setText('[{}]: {}'.format(sounds[3], ph[sounds[3]]))
                else:
                    self.label_sounds4.setText('{}: {}'.format(sounds[3], 'не определён'))
            elif n == 5:
                if sounds[0] in ph:
                    self.label_sounds1.setText('[{}]: {}'.format(sounds[0], ph[sounds[0]]))
                else:
                    self.label_sounds1.setText('{}: {}'.format(sounds[0], 'не определён'))
                if sounds[1] in ph:
                    self.label_sounds2.setText('[{}]: {}'.format(sounds[1], ph[sounds[1]]))
                else:
                    self.label_sounds2.setText('{}: {}'.format(sounds[1], 'не определён'))
                if sounds[2] in ph:
                    self.label_sounds3.setText('[{}]: {}'.format(sounds[2], ph[sounds[2]]))
                else:
                    self.label_sounds3.setText('{}: {}'.format(sounds[2], 'не определён'))
                if sounds[3] in ph:
                    self.label_sounds4.setText('[{}]: {}'.format(sounds[3], ph[sounds[3]]))
                else:
                    self.label_sounds4.setText('{}: {}'.format(sounds[3], 'не определён'))
                if sounds[4] in ph:
                    self.label_sounds5.setText('[{}]: {}'.format(sounds[4], ph[sounds[4]]))
                else:
                    self.label_sounds5.setText('{}: {}'.format(sounds[4], 'не определён'))
            elif n == 6:
                if sounds[0] in ph:
                    self.label_sounds1.setText('[{}]: {}'.format(sounds[0], ph[sounds[0]]))
                else:
                    self.label_sounds1.setText('{}: {}'.format(sounds[0], 'не определён'))
                if sounds[1] in ph:
                    self.label_sounds2.setText('[{}]: {}'.format(sounds[1], ph[sounds[1]]))
                else:
                    self.label_sounds2.setText('{}: {}'.format(sounds[1], 'не определён'))
                if sounds[2] in ph:
                    self.label_sounds3.setText('[{}]: {}'.format(sounds[2], ph[sounds[2]]))
                else:
                    self.label_sounds3.setText('{}: {}'.format(sounds[2], 'не определён'))
                if sounds[3] in ph:
                    self.label_sounds4.setText('[{}]: {}'.format(sounds[3], ph[sounds[3]]))
                else:
                    self.label_sounds4.setText('{}: {}'.format(sounds[3], 'не определён'))
                if sounds[4] in ph:
                    self.label_sounds5.setText('[{}]: {}'.format(sounds[4], ph[sounds[4]]))
                else:
                    self.label_sounds5.setText('{}: {}'.format(sounds[4], 'не определён'))
                if sounds[5] in ph:
                    self.label_sounds6.setText('[{}]: {}'.format(sounds[5], ph[sounds[5]]))
                else:
                    self.label_sounds6.setText('{}: {}'.format(sounds[5], 'не определён'))
            elif n == 7:
                if sounds[0] in ph:
                    self.label_sounds1.setText('[{}]: {}'.format(sounds[0], ph[sounds[0]]))
                else:
                    self.label_sounds1.setText('{}: {}'.format(sounds[0], 'не определён'))
                if sounds[1] in ph:
                    self.label_sounds2.setText('[{}]: {}'.format(sounds[1], ph[sounds[1]]))
                else:
                    self.label_sounds2.setText('{}: {}'.format(sounds[1], 'не определён'))
                if sounds[2] in ph:
                    self.label_sounds3.setText('[{}]: {}'.format(sounds[2], ph[sounds[2]]))
                else:
                    self.label_sounds3.setText('{}: {}'.format(sounds[2], 'не определён'))
                if sounds[3] in ph:
                    self.label_sounds4.setText('[{}]: {}'.format(sounds[3], ph[sounds[3]]))
                else:
                    self.label_sounds4.setText('{}: {}'.format(sounds[3], 'не определён'))
                if sounds[4] in ph:
                    self.label_sounds5.setText('[{}]: {}'.format(sounds[4], ph[sounds[4]]))
                else:
                    self.label_sounds5.setText('{}: {}'.format(sounds[4], 'не определён'))
                if sounds[5] in ph:
                    self.label_sounds6.setText('[{}]: {}'.format(sounds[5], ph[sounds[5]]))
                else:
                    self.label_sounds6.setText('{}: {}'.format(sounds[5], 'не определён'))
                if sounds[6] in ph:
                    self.label_sounds7.setText('[{}]: {}'.format(sounds[6], ph[sounds[6]]))
                else:
                    self.label_sounds7.setText('{}: {}'.format(sounds[6], 'не определён'))
            elif n == 8:
                if sounds[0] in ph:
                    self.label_sounds1.setText('[{}]: {}'.format(sounds[0], ph[sounds[0]]))
                else:
                    self.label_sounds1.setText('{}: {}'.format(sounds[0], 'не определён'))
                if sounds[1] in ph:
                    self.label_sounds2.setText('[{}]: {}'.format(sounds[1], ph[sounds[1]]))
                else:
                    self.label_sounds2.setText('{}: {}'.format(sounds[1], 'не определён'))
                if sounds[2] in ph:
                    self.label_sounds3.setText('[{}]: {}'.format(sounds[2], ph[sounds[2]]))
                else:
                    self.label_sounds3.setText('{}: {}'.format(sounds[2], 'не определён'))
                if sounds[3] in ph:
                    self.label_sounds4.setText('[{}]: {}'.format(sounds[3], ph[sounds[3]]))
                else:
                    self.label_sounds4.setText('{}: {}'.format(sounds[3], 'не определён'))
                if sounds[4] in ph:
                    self.label_sounds5.setText('[{}]: {}'.format(sounds[4], ph[sounds[4]]))
                else:
                    self.label_sounds5.setText('{}: {}'.format(sounds[4], 'не определён'))
                if sounds[5] in ph:
                    self.label_sounds6.setText('[{}]: {}'.format(sounds[5], ph[sounds[5]]))
                else:
                    self.label_sounds6.setText('{}: {}'.format(sounds[5], 'не определён'))
                if sounds[6] in ph:
                    self.label_sounds7.setText('[{}]: {}'.format(sounds[6], ph[sounds[6]]))
                else:
                    self.label_sounds7.setText('{}: {}'.format(sounds[6], 'не определён'))
                if sounds[7] in ph:
                    self.label_sounds8.setText('[{}]: {}'.format(sounds[7], ph[sounds[7]]))
                else:
                    self.label_sounds8.setText('{}: {}'.format(sounds[7], 'не определён'))
            elif n == 9:
                if sounds[0] in ph:
                    self.label_sounds1.setText('[{}]: {}'.format(sounds[0], ph[sounds[0]]))
                else:
                    self.label_sounds1.setText('{}: {}'.format(sounds[0], 'не определён'))
                if sounds[1] in ph:
                    self.label_sounds2.setText('[{}]: {}'.format(sounds[1], ph[sounds[1]]))
                else:
                    self.label_sounds2.setText('{}: {}'.format(sounds[1], 'не определён'))
                if sounds[2] in ph:
                    self.label_sounds3.setText('[{}]: {}'.format(sounds[2], ph[sounds[2]]))
                else:
                    self.label_sounds3.setText('{}: {}'.format(sounds[2], 'не определён'))
                if sounds[3] in ph:
                    self.label_sounds4.setText('[{}]: {}'.format(sounds[3], ph[sounds[3]]))
                else:
                    self.label_sounds4.setText('{}: {}'.format(sounds[3], 'не определён'))
                if sounds[4] in ph:
                    self.label_sounds5.setText('[{}]: {}'.format(sounds[4], ph[sounds[4]]))
                else:
                    self.label_sounds5.setText('{}: {}'.format(sounds[4], 'не определён'))
                if sounds[5] in ph:
                    self.label_sounds6.setText('[{}]: {}'.format(sounds[5], ph[sounds[5]]))
                else:
                    self.label_sounds6.setText('{}: {}'.format(sounds[5], 'не определён'))
                if sounds[6] in ph:
                    self.label_sounds7.setText('[{}]: {}'.format(sounds[6], ph[sounds[6]]))
                else:
                    self.label_sounds7.setText('{}: {}'.format(sounds[6], 'не определён'))
                if sounds[7] in ph:
                    self.label_sounds8.setText('[{}]: {}'.format(sounds[7], ph[sounds[7]]))
                else:
                    self.label_sounds8.setText('{}: {}'.format(sounds[7], 'не определён'))
                if sounds[8] in ph:
                    self.label_sounds9.setText('[{}]: {}'.format(sounds[8], ph[sounds[8]]))
                else:
                    self.label_sounds9.setText('{}: {}'.format(sounds[8], 'не определён'))
            elif n == 10:
                if sounds[0] in ph:
                    self.label_sounds1.setText('[{}]: {}'.format(sounds[0], ph[sounds[0]]))
                else:
                    self.label_sounds1.setText('{}: {}'.format(sounds[0], 'не определён'))
                if sounds[1] in ph:
                    self.label_sounds2.setText('[{}]: {}'.format(sounds[1], ph[sounds[1]]))
                else:
                    self.label_sounds2.setText('{}: {}'.format(sounds[1], 'не определён'))
                if sounds[2] in ph:
                    self.label_sounds3.setText('[{}]: {}'.format(sounds[2], ph[sounds[2]]))
                else:
                    self.label_sounds3.setText('{}: {}'.format(sounds[2], 'не определён'))
                if sounds[3] in ph:
                    self.label_sounds4.setText('[{}]: {}'.format(sounds[3], ph[sounds[3]]))
                else:
                    self.label_sounds4.setText('{}: {}'.format(sounds[3], 'не определён'))
                if sounds[4] in ph:
                    self.label_sounds5.setText('[{}]: {}'.format(sounds[4], ph[sounds[4]]))
                else:
                    self.label_sounds5.setText('{}: {}'.format(sounds[4], 'не определён'))
                if sounds[5] in ph:
                    self.label_sounds6.setText('[{}]: {}'.format(sounds[5], ph[sounds[5]]))
                else:
                    self.label_sounds6.setText('{}: {}'.format(sounds[5], 'не определён'))
                if sounds[6] in ph:
                    self.label_sounds7.setText('[{}]: {}'.format(sounds[6], ph[sounds[6]]))
                else:
                    self.label_sounds7.setText('{}: {}'.format(sounds[6], 'не определён'))
                if sounds[7] in ph:
                    self.label_sounds8.setText('[{}]: {}'.format(sounds[7], ph[sounds[7]]))
                else:
                    self.label_sounds8.setText('{}: {}'.format(sounds[7], 'не определён'))
                if sounds[8] in ph:
                    self.label_sounds9.setText('[{}]: {}'.format(sounds[8], ph[sounds[8]]))
                else:
                    self.label_sounds9.setText('{}: {}'.format(sounds[8], 'не определён'))
                if sounds[9] in ph:
                    self.label_sounds10.setText('[{}]: {}'.format(sounds[9], ph[sounds[9]]))
                else:
                    self.label_sounds10.setText('{}: {}'.format(sounds[9], 'не определён'))
            elif n > 10:
                self.label_sounds1.setText('Слишком много звуков!')












def main():
    app = QApplication(sys.argv)
    entry = Beginning()
    entry.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()