with open('../resources/ips.txt', 'r') as file:
    for l in file.readlines():
        x = l.rstrip().split('.')
        if int(x[2]) < 100 and int(x[3]) < 100: print(l)