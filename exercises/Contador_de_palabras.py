# https://pywombat.com/my/exercises/483c06ab

def contador(string):
    words = {}
    string = string.replace('.', '').replace(',', '').split(' ')
    for word in string:
        words[word] = words.get(word, 0) + 1 if word in words else 1
    return words


if __name__ == '__main__':
    print(contador('Hola mundo'))
    print(contador('PyWombat, una plataforma de ejercicios de Python. PyWombat.'))