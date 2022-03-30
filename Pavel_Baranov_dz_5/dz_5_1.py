# 1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
def nums_generator(max_num):
    for num in range(1, max_num + 1, 2):
        yield num


nums_gen = nums_generator(30)
print(next(nums_gen), next(nums_gen), next(nums_gen), sep=', ')
