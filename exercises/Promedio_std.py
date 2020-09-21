from math import sqrt

def promedio_std(lista):
    sumatoria = sum(lista)
    n = len(lista)
    promedio = sumatoria/n
    cuadrado_menos_promedio = []
    for num in lista:
        cuadrado_menos_promedio.append((num-promedio)**2)
    varianza = sum(cuadrado_menos_promedio)/n
    desviacion = sqrt(varianza)
    return promedio, desviacion


print(promedio_std([1,2,3,4,5,6,7]))