# https://pywombat.com/my/exercises/1694b2f6

def vocales(arr):
    vowels = 'aeiou'
    l = []
    for string in arr:
        for vowel in vowels:
            if vowel in string.lower():
                l.append(string)
                break
    return l

if __name__ == '__main__':
    print(vocales(['Hola', 'ffff', 'zzzz', 'AAAAA']))
    print(vocales(['Eduardo', 'Py', 'PyWombat']))
