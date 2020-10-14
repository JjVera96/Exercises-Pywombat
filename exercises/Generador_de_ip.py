import random

def generateIP():
    return '{}.{}.{}.{}'.format(random.randint(0,256),random.randint(0,256),random.randint(0,256),random.randint(0,256))

num = int(input('Cantidad de IPs a generar: '))
l = []
while(len(l) < num):
    ip = generateIP()
    if not ip in l:
        l.append(ip)
        print(ip)