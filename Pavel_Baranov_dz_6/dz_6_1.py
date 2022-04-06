# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
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

