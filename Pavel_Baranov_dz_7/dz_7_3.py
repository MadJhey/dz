"""
Task3
Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или
«руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку
templates, например:
|--my_project
   ...
   |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
"""
import os
import shutil

source = 'my_project'
destination = 'templ'
num = 0
for root, dirs, files in os.walk(source):

    for dir in dirs:

        # print(root)
        # print(dir)
        if 'templates' in dir:
            num += 1
            try:
                shutil.copytree(os.path.join(root, dir), os.path.join(destination, dir + str(num)))
            except FileExistsError:
                print("Такой каталог уже существует")
