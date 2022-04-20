"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""
import random
import time


class Card:
    def __init__(self):
        self.matrix = []
        self.amount = 15
        list_num = list(range(1, 91))
        random.shuffle(list_num)

        for _ in range(3):

            # генерируем позиции в строке
            poz_list = sorted(random.sample(list(range(1, 10)), k=5))
            # заполняем позиции

            line = []
            for i in range(9):
                if i + 1 in poz_list:
                    line.append(list_num.pop())
            line.sort()
            for i in range(9):
                if not (i + 1 in poz_list):
                    line.insert(i, " ")

            self.matrix.append(line)

    def print(self):
        for i in range(3):
            print(' '.join(map(lambda x: '%2s' % x, self.matrix[i])))
        print('----------------------------')

    def _find_value(self, value):
        for i in range(3):
            try:
                ind = self.matrix[i].index(value)
                return (i, ind)
            except ValueError:
                pass
        return (None)


class Player:
    def __init__(self, is_computer, name):
        self._is_computer = is_computer
        self._name = name
        self._ingame = True

    def __str__(self):
        return (f'name: {self._name}, ' + ('computer' if self._is_computer else 'player'))


class Game:
    def __init__(self, *players):
        self.players = players
        self.box = list(range(1, 91))
        random.shuffle(self.box)

    def _round(self):
        value = self.box.pop()
        print(f'Значение {value} осталось {len(self.box)}')
        for pl in self.players:
            if not pl._ingame:
                continue
            print(pl)
            print('----------------------------')
            pl.card.print()
            find_value = pl.card._find_value(value)
            if not find_value == None:
                pl.card.matrix[find_value[0]][find_value[1]] = '-'
                pl.card.amount -= 1
                if not pl._is_computer and pl._ingame:
                    if input(f'Зачеркнуть цифру {value}? (y/n) ') == 'n':
                        print(f'Игрок {pl} проиграл и вышел из игры! Пропущена цифра!')
                        pl._ingame = False
                        time.sleep(2)
                        return (True)
                if pl.card.amount == 0:
                    print(f'Победил {pl}')
                    return (False)
            else:
                if not pl._is_computer and pl._ingame:
                    if input(f'Зачеркнуть цифру {value}? (y/n) ') == 'y':
                        print(f'Игрок {pl} проиграл и вышел из игры! Нет такой цифры!')
                        pl._ingame = False
                        time.sleep(2)
                        return (True)

        return (True)

    @property
    def start(self):
        # инициализация карт
        for pl in self.players:
            pl.card = Card()
        # игра
        while len(self.box) > 0:
            if not self._round():
                break

    @property
    def stop(self):
        pass

    @property
    def pause(self):
        pass


pl1 = Player(True, 'win64')
pl2 = Player(True, 'mac')
pl3 = Player(False, 'Petr')

game = Game(pl1, pl2, pl3)
game.start
