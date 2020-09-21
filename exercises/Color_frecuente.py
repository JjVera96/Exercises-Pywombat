def color_frecuente(lista):
    prioridad = ["azul","rojo","verde","amarillo"]
    color_mas_repetido = None
    veces_mas_repetido = 0
    for color in prioridad:
        veces = lista.count(color)
        if veces > veces_mas_repetido:
            veces_mas_repetido = veces
            color_mas_repetido = color
    return color_mas_repetido, veces_mas_repetido

colores = ['azul', 'rojo', 'verde', 'verde', 'verde', 'rojo', 
           'verde', 'verde', 'azul', 'amarillo', 'azul',
           'azul', 'verde', 'verde', 'verde', 'amarillo']

print(color_frecuente(colores))