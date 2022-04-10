"""Task2
*(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со
следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html


Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом
текстовом редакторе «руками» (не программно); предусмотреть возможные исключительные
ситуации, библиотеки использовать нельзя.
"""


import yaml
import os


def list_dict(data):
    # print(type(data))
    if type(data) is dict:
        for folder,v in data.items():
            try:
                print("key:\t" + folder)
                if not os.path.exists(folder):
                    os.mkdir(folder)
                os.chdir(folder)
                list_dict(v)
            except AttributeError:
                print("ошибка:\t" + str(v))
                return
    elif type(data) is list:
        for x in data:
            print(x)
            if '.' in x:
                f = open(x, 'w')
                f.close()
            else:
                list_dict(x)
        os.chdir('../')


with open('config.yaml') as f:
    ya = yaml.safe_load(f)
    print(ya)
    list_dict(ya)




