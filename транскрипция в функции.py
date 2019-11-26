def transcription(word):

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
    return trnscrpt

# print(transcription('помогите'))