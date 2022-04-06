# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов
# и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь
# в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше
# записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из
# скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз
# меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# **(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было
# задать имя обоих исходных файлов и имя выходного файла. Проверить работу скрипта.
import itertools
import sys
file1 = sys.argv[1]
file2 = sys.argv[2]
file3 = sys.argv[3]

with open(f"{file1}.csv", mode='r', encoding='utf-8') as users:
    with open(f"{file2}.csv", mode='r', encoding='utf-8') as hobbys:
        am_users = sum(1 for _ in users)
        am_hobbys = sum(1 for _ in hobbys)
        if am_users < am_hobbys:
            exit(1)
        users.seek(0)
        hobbys.seek(0)
        rez = {}
        for user, hobby in itertools.zip_longest(users, hobbys, fillvalue=None):
            rez[user.strip()] = f'{hobby}'.strip()
with open(f"{file3}.csv", mode='w', encoding='utf-8') as file3:
    for x in rez.items():
        print(x,file=file3)
# python dz_6_4.py users hobby rez
