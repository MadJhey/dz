# 1
massive = list()
range_1000 = range(1, 1001, 2)
for amount in range_1000:
    massive.append(amount ** 3)

sum_all = 0
for amount in massive:
    sum_number = 0
    # sum_number = map(int, str(amount))
    # sum_number = sum(sum_number)
    for number in str(amount):
        sum_number = sum_number + int(number)
    if sum_number % 7 == 0:
        sum_all = sum_all + amount
        # print(sum_number, amount, sum_all)
print(sum_all)
sum_all = 0
for amount in massive:
    sum_number = 0
    # sum_number = map(int, str(amount+17))
    # sum_number = sum(sum_number)
    for number in str(amount+17):
        sum_number = sum_number + int(number)
    if sum_number % 7 == 0:
        sum_all = sum_all + amount
        # print(sum_number, amount, sum_all)
print(sum_all)