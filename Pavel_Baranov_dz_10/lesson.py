class Car:
    def __init__(self):
        self.modules = []
        self.fc = 7

    def __call__(self, price=None):
        print(f'РЎС„РѕСЂРјРёСЂРѕРІР°РЅ Р·Р°РєР°Р· СЃ РјРѕРґСѓР»СЏРјРё {self.modules} Рё С†РµРЅРѕР№ {price}')

    def __str__(self):
        return f'{self.modules}'  # str!

    def __add__(self, other):
        self.modules.append(other)
        return self

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        # self.__dict__[key] = value
        print(f'Р”РѕР±Р°РІР»СЏРµС‚СЃСЏ Р°С‚СЂРёР±СѓС‚ {key} СЃРѕ Р·РЅР°С‡РµРЅРёРµРј {value}')

    def __getitem__(self, item):
        return self.modules[item]

    def __eq__(self, other):
        return self.fc == other

    def __del__(self):
        print('РѕР±СЉРµРєС‚ СѓРґР°Р»РµРЅ')


# car = Car()
# car + 'С‚РµРїР»С‹Р№ СЂСѓР»СЊ' + 'РјР°РіРЅРёС‚РѕР»Р°' + 'РґРІРёРіР°С‚РµР»СЊ РЅР° РґСЂРѕРІР°С…'
# car.model = 'Tesla'
# print(car[1])
# car(price=50000)
# car()
#
# print(car == 6)


# from abc import ABC, abstractmethod
#
#
# class MyAbcClass(ABC):
#
#     @abstractmethod
#     def my_method_1(self):
#         pass
#
#     @abstractmethod
#     def my_method_2(self):
#         pass
#
#     def qwe(self):
#         print('qwe')
#
#
# class MyClass(MyAbcClass):
#     def my_method_1(self):
#         pass
#
#     def my_method_2(self):
#         pass
#
#
# mc = MyClass()
# mc.qwe()


# for i in [1, 2, 3, 4, 5]:
#     print(i)


# class Iterator:
#     def __init__(self):
#         self.i = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i <= 5:
#             return self.i
#         else:
#             raise StopIteration
#
#
# qwe = Iterator()
# for i in qwe:
#     print(i)


# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self._age = age
#
#     @property
#     def age(self):
#         # if check
#         return self._age
#
#
# # code
# human = Human('Alex', 20)
# print(human.age)


class WinDoor:
    def __init__(self, w, h):
        self.square = w * h


class Room:
    def __init__(self, l1, l2, h):
        self.square = 2 * h * (l1 + l2)
        self.wd = []

    def add_windoor(self, w, h):
        self.wd.append(WinDoor(w, h))

    def common_square(self):
        main_squre = self.square
        for el in self.wd:
            main_squre -= el.square
        return main_squre


r = Room(7, 4, 3)
print(r.square)
r.add_windoor(2, 2)
r.add_windoor(2, 2)
r.add_windoor(2, 3)
r.add_windoor(1, 2)
print(r.common_square())