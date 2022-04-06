import sys

pars = sys.argv[1:]
# pars = [2,3]
with open('bakery.csv', mode='r') as f:
    num = 0
    if len(pars) == 0:  # все выводим
        for x in f:
            print(x, end='')
    elif len(pars) == 1:
        for x in f:
            num += 1
            if int(pars[0]) <= num:
                print(x, end='')
    else:
        for x in f:
            num += 1
            if int(pars[0]) <= num <= int(pars[1]):
                print(x, end='')
