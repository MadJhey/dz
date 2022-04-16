"""
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        # print(self.name)

    def go(self):
        print(f'{self.name} едет прямо')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(self.name + " " + str(self.speed))


car1 = Car(60, 'red', 'ford', False)
car1.speed = 70
car1.show_speed()


class TownCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(self.name + " " + str(self.speed))
        if self.speed > 60:
            print(f'{self.name} превышена скорость')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        print(self.name + " " + str(self.speed))
        if self.speed > 40:
            print(f'{self.name} превышена скорость')


class PoliceCar(Car):
    pass


tc1 = TownCar(90, 'red', 'uaz')
tc1.show_speed()
print(f'Police {tc1.is_police}')
tc1.turn('направо')

sc1 = SportCar(120,'black', 'infiniti', False)
sc1.go()
sc1.stop()