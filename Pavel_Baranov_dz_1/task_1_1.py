# число  суток, часов, мин и пр. в дате
amount_sec = int(input('Введите число секунд: '))
dict_time = {'д.': 86400, 'ч.': 3600, 'мин.': 60, 'сек.': 1}
for key, value in dict_time.items():
    amount = amount_sec // value
    if amount > 0:
        print(f'{amount} {key}')
        amount_sec = amount_sec - amount * value