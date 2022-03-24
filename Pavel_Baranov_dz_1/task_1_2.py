# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.
massive = list()
range_1000 = range(1, 1001, 2)
for amount in range_1000:
    massive.append(amount ** 3)
sum_all = 0
for amount in massive:
    sum_number = 0
    for number in str(amount):
        sum_number = sum_number + int(number)
    if sum_number % 7 == 0:
        sum_all += amount
        # print(sum_number, amount, sum_all)
print(sum_all)
sum_all = 0
for amount in massive:
    sum_number = 0
    for number in str(amount+17):
        sum_number += int(number)
    if sum_number % 7 == 0:
        sum_all += amount
        # print(sum_number, amount, sum_all)
print(sum_all)