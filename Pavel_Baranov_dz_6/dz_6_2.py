# 2. *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла
# логов из предыдущего задания.
# Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать
# даже с файлами, размер которых превышает объем ОЗУ компьютера.

with open('nginx_logs.txt') as f:
    spam = []
    for line in f:
        sl = line.split(sep=" ")
        # print(line)
        # print(sl)
        # print(sl[0])
        # print(sl[5][1:])
        # print(sl[6])
        tp = (sl[0], sl[5][1:], sl[6])
        spam.append(sl[0])
        print(tp)
spam.sort(reverse=0)
print(spam[0], spam.count(spam[0]))

