# 4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции
# и выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...
#
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5

def val_checker(func):
    def wrapper(x):
        if x < 0:
            raise ValueError(f'wrong val {x}')
        result = func(x)
        return result

    return wrapper


# @val_checker(lambda x: x > 0)

@val_checker
def calc_cube(x):
    return x ** 3


print(calc_cube(-5))

# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
