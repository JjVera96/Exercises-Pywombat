# https://pywombat.com/my/exercises/b046585f

def string_counter(string):
    string = string.replace(' ','')
    return len(string)

if __name__ == '__main__':
    print(string_counter('Hola mundo'))
    print(string_counter('PyWombat'))
