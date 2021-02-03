"""
def calcular_area_circulo(radio):
    return 3.14 * (radio * radio)

def area_tringulo(base, altura):
    return (base * altura ) / 2

def division(dividendo, divisor):
    return dividendo / divisor

def promedio(*calificaciones):
    return sum(calificaciones) / len(calificaciones)

"""

def calcular_area_circulo(radio: float) -> float:
    return 3.14 * (radio * radio)

def area_tringulo(base: float, altura: float) -> float:
    return (base * altura ) / 2

def division(dividendo: float, divisor: float) -> float:
    return dividendo / divisor

def promedio(calificaciones: list) -> float:
    return sum(calificaciones) / len(calificaciones)

print(calcular_area_circulo(3.0))
print(area_tringulo(4.0, 3.0))
print(division(12.0, 4.0))
print(promedio([1.0, 2.0, 3.0]))