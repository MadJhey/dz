"""
1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя
и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли смысл
в данном случае использовать функцию re.compile()?

2. * (вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
для получения информации вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>,
<response_size>), например:

raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки?
Можно ли для них уточнить регулярное выражение?

"""
import re
import os


def email_parse(email):
    re_someone = re.compile(r'[A-Za-z]{1}[-0-9A-z\.]{1,}[0-9A-Za-z]{1}(?=@)')
    someone = re_someone.search(email).group(0)

    re_domain = re.compile(r'(?<=@)([-A-Za-z]{1,}\.){1,2}[-A-Za-z]{2,}')
    domain = re_domain.search(email).group(0)

    print(someone, domain)


email_parse('someone@geekbrains.ru')

os.system("pause")

patt = "((?:[0-9]{1,3}[\.]){3}[0-9]{1,3}).\-.\-.(\[.*?\]).\"(\w*?) (\/\w*\/\w* \w*\/\d.\d). (\d*) (\d)"
re_res = re.compile(patt)

with open('nginx_logs.txt') as f:
    spam = []
    f.seek(0)
    for line in f:
        res = re_res.findall(line)
        print(res)
        spam.append(res)

# print(spam, sep='\n')
