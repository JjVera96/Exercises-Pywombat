string = input("Ingresa una palabra/sentencia: ")

for letter in string:
    if letter in 'aeiouAEIOU':
        print(letter, end='')