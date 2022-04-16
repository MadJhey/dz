"""
1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

import time


class TrafficLight:

    def __init__(self):
        self._color = {1: 'красный', 2: 'жёлтый', 3: 'зелёный'}
        self.current = 0
        self.time = 0

    def __running(self):

        self.current += 1
        if self.current == 4:
            self.current = 1

        if self.current == 1:
            self.time = 3
        elif self.current == 2:
            self.time = 2
        else:
            self.time = 1

        print(f'{self._color[self.current]} {self.time}')
        time.sleep(self.time)


tl = TrafficLight()

for i in range(0, 6):
    # tl.running()
    tl._TrafficLight__running()
