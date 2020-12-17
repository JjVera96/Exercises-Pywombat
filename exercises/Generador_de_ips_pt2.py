import sys
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
        
if not "--notfile" in sys.argv:
    with open("../resources/ips_v2.txt", 'w') as file:
        for ip in l: file.write(ip+"\n")