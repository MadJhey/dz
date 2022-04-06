import sys

amount = sys.argv[1]
# amount =  11
with open('bakery.csv', mode='a') as f:
    f.write(f'{str(amount)}\n')
