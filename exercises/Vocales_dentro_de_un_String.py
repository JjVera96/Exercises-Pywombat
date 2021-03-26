string = input('Ingresa una palabra/sentencia: ')

vowels = { 'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0 }

for letter in string:
    if letter.lower() in 'aeiou':
        print(letter, end='')
        vowels[letter.lower()] += 1

print('\nLas vocales son:')
for key, value in vowels.items():
    print('{}: {}'.format(key, value))
