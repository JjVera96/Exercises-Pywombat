from datetime import datetime

if __name__ == '__main__':
    h1 = int(input(''))
    m1 = int(input(''))
    s1 = int(input(''))

    h2 = int(input(''))
    m2 = int(input(''))
    s2 = int(input(''))

    dh = h2-h1
    dm = m2-m1
    ds = s2-s1

    seconds = (dh*3600) + (dm*60) + (ds)
    
    print(seconds)
