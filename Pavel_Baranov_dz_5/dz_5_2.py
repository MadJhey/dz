# 2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
max_num = input('Введите число: ')
nums_gen = (num for num in range(1, int(max_num) + 1, 2))
print(next(nums_gen), next(nums_gen), next(nums_gen), sep=', ')
