words = ["процент", 'процента', 'процента', 'процента', 'процентов', 'процентов', 'процентов', 'процентов', 'процентов']
id_words = range(1, 101)
for i in id_words:
    if i != 11 and i != 12 and i != 13 and i != 14:
        id_words = i - i//10*10
        # print(id_words)
        value = words[id_words-1]
    else:
        value = 'процентов'
    print(i, value)