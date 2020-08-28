def contar_letras(cadena):
    i = 0
    letra = cadena[i]
    cant = 0
    while(True):
        cant += 1
        try:
            i += 1
            letra = cadena[i]
            
        except:
            break
    return cant
    
x = input('Ingresa un texto: ')
print(contar_letras(x))