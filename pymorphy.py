import pymorphy2
def give_info_about_word(w):
    morph = pymorphy2.MorphAnalyzer()
    show = []
    p = morph.parse(w)[0]
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

    return show

print(give_info_about_word('хорош'))