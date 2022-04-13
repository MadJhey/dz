"""
3. Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...


@type_logger
def calc_cube(x):
   return x ** 3

# >>> a = calc_cube(5)
5: <class 'int'>
Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
calc_cube(5: <class 'int'>)
"""
from functools import wraps

def type_logger(func):
    print(1)

    # @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(2)
        print(args)
        print(kwargs)
        print(f'{func.__name__}({", ".join(map(str, args))}): {type(args)}')
        print(f'{func.__name__}({args[0]}: {type(args[0])}')
        print(f'a = call {func.__name__}({", ".join(map(str, args))})')

        return result

    return wrapper


@type_logger
def calc_cube(y, x):
    return x ** 3 * y


print(calc_cube(6, x=5))
