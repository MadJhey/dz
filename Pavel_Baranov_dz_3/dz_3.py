# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one") # "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.
# 2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"
dict1 = {
    "one": "один", "two": "два", "three": "три",
    "four": "четыре", "five": "пять", "six": "шесть",
    "seven": "семь", "eight": "восемь", "nine": "девять",
    "ten": "десять"
}


def num_translate_adv(par):
    ret = dict1.get(par.lower())
    if ret == None:
        return None
    else:
        if par[0].isupper():
            return ret.title()
        else:
            return ret


print(num_translate_adv("one"))
print(num_translate_adv("Five"))


# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
# >>>  thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам? Можно ли использовать словарь в этом случае?


def check(key, list_name):
    rez = []
    for name in list_name:
        if key == name[0]:
            rez.append(name)
    # rez = filter(lambda x: x[0] == key, list_name)
    return rez


def thesaurus(*args):
    rez = {}
    for name in args:
        letter = name[0]
        rez.setdefault(letter, list(check(letter, args)))
    sorted(rez)
    return rez


def thesaurus1(*names):
    out_dict = dict()
    for name in names:
        out_dict.setdefault(name[0], [])
        out_dict[name[0]].append(name)
    return out_dict


from time import perf_counter

start = perf_counter()
print(thesaurus("Иван", "Мария", "Петр", "Илья"))
end = perf_counter()
print(f'Мой вариант {end - start}')
start = perf_counter()
print(thesaurus1("Иван", "Мария", "Петр", "Илья"))
end = perf_counter()
print(f'Не мой вариант {end - start}')
print(f'Мой вариант сравним, вариант через lambda функцию медленее в 2 раза')

# 4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "И": {
#         "И": ["Илья Иванов"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
# Как поступить, если потребуется сортировка по ключам?

def thesaurus_adv(*names_surnames):
    out_dict = {}
    for name_surname in names_surnames:
        name, surname = name_surname.split()
        out_dict.setdefault(surname[0], {})
        out_dict[surname[0]].setdefault(name[0], [])
        out_dict[surname[0]][name[0]].append(name_surname)

    # sort example
    sorted_dict = {x: out_dict[x] for x in sorted(out_dict)}  # Dict Comprehensions
    return out_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов",
                    "Анна Савельева"))


# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
# Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное ДЗ.

def get_jokes(amount, sign):
    """
    Функция возвращает шутки
    :param amount:
        число, возвращаемых шуток
    :param sign:
        флаг без повторов
    :return:
        список сгенерированных шуток
    """
    # глобальные переменные - ересь :)
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    import random
    rez = []
    if min(len(nouns), len(adverbs), len(adjectives)) < amount:
        return f'Недостаточно данных! Ошибка!'
    if sign:
        noun = random.sample(nouns, amount)
        adverb = random.sample(adverbs, amount)
        adjective = random.sample(adjectives, amount)
    else:
        noun = random.choices(nouns, k=amount)
        adverb = random.choices(adverbs, k=amount)
        adjective = random.choices(adjectives, k=amount)
    i = 0
    while i <= amount - 1:
        rez.append(f'{noun[i]} {adverb[i]} {adjective[i]}')
        i += 1
    return rez


print(get_jokes(5, 1))
print(get_jokes(5, False))
