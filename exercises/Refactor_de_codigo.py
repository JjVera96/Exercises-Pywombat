# https://pywombat.com/my/exercises/c988e2d9

"""
    promedio = 0
    total = 0
    cantidad = 101

    for n in range(1, cantidad):
        total = total + n

    promedio = total / cantidad

    print(promedio)
"""

if __name__ == '__main__':
    promedio = total = 0
    cantidad = 101
    promedio = sum(range(1, cantidad))/cantidad
    print(promedio)
    