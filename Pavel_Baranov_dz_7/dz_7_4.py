"""
Task4
Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
а значения — общее количество файлов (в том числе и в подпапках), размер которых
не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }

Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

*(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде
словаря, в котором ключи те же, а значения — кортежи вида
(<files_quantity>, [<files_extensions_list>]), например:
    {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }

Сохраните результаты в файл <folder_name>_summary.json в той же папке,
где запустили скрипт.
"""

import os
import json

# os.chdir('my_project')

data = []
# сбор данных
for root, dir, fls in os.walk('./'):
    for file in fls:
        file_path = os.path.join(root, file)
        st_size = os.stat(file_path).st_size
        size = 10 ** len(str(st_size))
        size = max(100, size)
        data.append((file_path, file_path.split('.')[-1], st_size, size))

dc = {}

for file in data:
    dc.setdefault(file[3], [0, []])  # инициализация пустого словаря
    dc[file[3]][0] += 1  # подсчет файлов
    dc[file[3]][1].append(file[1])  # сбор расширений

for key in dc:
    dc[key][1] = list(set(dc[key][1]))  # свертка расширений

dc = dict(sorted(dc.items(), key=lambda x: x[0]))  # сортировка словаря

print(dc)

with open('file_stat_dz7.json', 'w') as f:
    json.dump(dc, f)
