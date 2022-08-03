# https://pywombat.com/my/exercises/21a01460

def contador_substrings(string, substring):
    times = string.split(substring)
    return len(times)-1

if __name__ == '__main__':
    print(contador_substrings('Hola mundo', 'o'))
    print(contador_substrings('Nuevo ejercicio en PyWombat', 'ue'))
    print(contador_substrings('Contador de caracteres', 'de'))
    print(contador_substrings('PyWombat Ejercicios de Python con extensión Py', 'Py'))