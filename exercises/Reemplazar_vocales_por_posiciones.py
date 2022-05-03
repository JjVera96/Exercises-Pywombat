# https://pywombat.com/my/exercises/53aee14f

if __name__ == '__main__':
    string = input('Cadena: ')

    vowels = {
        'a': 1,
        'e': 2,
        'i': 3,
        'o': 4,
        'u': 5
    }

    result = ''
    for x in string:
        if x in 'aeiouAEIOU':
           x = vowels[x.lower()] 
        result += str(x)
        
    print(result)
    