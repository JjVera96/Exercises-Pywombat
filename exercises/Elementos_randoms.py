import random

personas = ['Eduardo', 'Raquel', 'Roberto', 'Marines', 'Isabel']
random.shuffle(personas)

for index, persona in enumerate(personas):
    print('{} - {}'.format(index, persona))    