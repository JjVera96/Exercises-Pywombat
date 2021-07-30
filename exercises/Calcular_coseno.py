from math import cos

def coseno(value):
    return round(cos(value), 11)

if __name__ == '__main__':
    print(coseno(120))
    print(coseno(87))
