# https://pywombat.com/my/exercises/fc546fe0

def vocales(string):
    return [x for x in string if x in 'aeiouAEIOU']

if __name__ == '__main__':
    print(vocales('Hola mundo'))
    print(vocales('Nuevo tutorial'))
    print(vocales('Ejercicio PyWombat'))