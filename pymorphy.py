import pymorphy2
def give_info_about_word(w):
    morph = pymorphy2.MorphAnalyzer()
    show = []
    p = morph.parse(w)[0]
    poses = {'VERB': 'глагол', 'NOUN': 'имя существительное', 'ADJF': 'имя прилагательное',
             'ADJS': 'имя прилагательное (краткое)', 'INFN': 'глагол (инфинитив)', 
             'PRTF': 'причастие (полное)', 'PRTS': 'причастие (краткое)', 'GRND': 'деепричастие',
             'NUMR': 'числительное', 'ADVB': 'наречие', 'NPRO': 'местоимение', 
             'PREP': 'предлог', 'CONJ': 'союз', 'PRCL': 'частица', 'INTJ': 'междометие'}
    if p.tag.POS in poses:
        show.append(poses[p.tag.POS])

    if show[0] == 'имя существительное':
        # определение падежа
        padezh = p.tag.case
        cases = {'nomn': 'именительный', 'gent': 'родительный', 'datv': 'дательный',
                 'accs': 'винительный', 'ablt': 'творительный', 'loct': 'предложный',
                 'voct': 'звательный'}
        if padezh in cases:
            show.append(cases[padezh])
        else:
            show.append('падеж не определён')
        # определение числа
        numer = p.tag.number
        numbers = {'sing': 'единственное число', 'plur': 'множественное число',
                   'only sing': 'только единственное число', 'only plur': 'только множественное число'}
        #if 'Sgtm sing' in 
        #show.append(numbers[numer])
        # определение рода
        #genders = {'masc': 'мужской род', 'femn': 'женский род', 'neut': 
        

    return show

print(give_info_about_word('брюки'))