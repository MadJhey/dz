import sys


def _get(lst, name, value):
    for curr in lst:
        if curr.get('CharCode') == name:
            return curr.get(value)
    else:
        return None

def currency_rates(name_curr):
    from requests import get
    from xmltodict import parse
    from datetime import datetime
    from decimal import Decimal

    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    if not response:
        return (f'Не работает сервер валюты!')
    dict_data = parse(response.content)
    ValCurs = dict_data.get("ValCurs")
    date = None
    value = None
    if ValCurs != None:
        dateStr = ValCurs.get('@Date')
        values_list = ValCurs.get('Valute')
        valueStr = _get(values_list, name_curr.upper(), 'Value')
        if valueStr and dateStr:
            dateFormatter = "%d.%m.%Y"
            date = datetime.strptime(dateStr, dateFormatter)
            value = Decimal(valueStr.replace(',', '.'))
    return (f'{value} {date}')


if len(sys.argv) >= 2:
    name_curr = sys.argv[1]
    print(currency_rates(name_curr))
