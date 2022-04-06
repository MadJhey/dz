# . Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration
# в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
amount_sec = int(input('Введите число секунд: '))
dict_time = {'дн': 86400, 'час': 3600, 'мин': 60, 'сек': 1}
for key, value in dict_time.items():
    amount = amount_sec // value
    if amount > 0:
        print(f'{amount} {key}')
        amount_sec = amount_sec - amount * value