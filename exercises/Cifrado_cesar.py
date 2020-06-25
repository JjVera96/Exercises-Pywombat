import string

letras = string.ascii_lowercase

def cifrado(sentencia=None, llave=10):
    sentencia = sentencia.lower()
    sentencia_cifrada = ''
    for letra in sentencia:
        if letra in letras:
            index = letras.index(letra)
            index = (index+llave)%len(letras)
            sentencia_cifrada += letras[index]
        else:
            sentencia_cifrada += letra
    return sentencia_cifrada
    
print(cifrado('Hola Como estas', 23))
print(cifrado('supersentencia'))
print(cifrado('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 23))
