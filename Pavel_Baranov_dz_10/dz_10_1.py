"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
 который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
| 31 22 |
| 37 43 |
| 51 86 |

| 3 5 32 |
| 2 4 6 |
| -1 64 -8 |

| 3 5 8 3 |
| 8 3 7 1 |
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно.
Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.
"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def show(self):
        print(self.matrix)

    def __add__(self, other):
        if isinstance(other, Matrix):

            tmp = [map(sum, zip(*i)) for i in zip(self.matrix, other.matrix)]
            # здесь получает список итераций map
            # не смог его преобразовать в list в одной строке, пришлось делать преобразование в цикле
            self.matrix = []
            for x in tmp:
                self.matrix.append(list(x))

            # result = [[self.matrix[i][j] + other.matrix[i][j] for j in range
            # (len(self.matrix[0]))] for i in range(len(self.matrix))]
        else:
            print("wrong value")
        return self

    def __str__(self):
        res = ''
        for i in self.matrix:
            res += str(i)+'\n'
        return res

m1 = Matrix([[1, 2, 3], [4, 5, 6]])
print(m1)

m1 + 5
m2 = Matrix([[11, 12, 13], [14, 15, 100]])
m3 = Matrix([[11, 12], [ 15, 100]])
m1 + m2 + m1

print(m1)

m1+m3
print(m1)