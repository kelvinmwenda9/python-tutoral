import random

filed = input('enter file name: ')

with open(filed, 'r') as file:
    data = file.read()
    print(data)
    # convert txt into list values
    data_f = data.split('\n')
    print(data_f)

    print(random.choice(data_f))