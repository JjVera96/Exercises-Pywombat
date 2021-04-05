def count_vowels(string):
    counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for letter in string:
        if letter.lower() in list(counts.keys()):
            counts[letter.lower()] += 1
    return counts

def main():
    string = input('Ingresa una frase o palabra: ')
    vowels = count_vowels(string)

    print('Las vocales son:')
    for key, value in vowels.items():
        print('{}: {}'.format(key, value))

if __name__ == '__main__':
    main()
