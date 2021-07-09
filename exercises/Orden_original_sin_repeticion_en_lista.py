if __name__ == '__main__':
    sentence = input('Secuencia: ')
    result = [sentence[0]]
    for letter in sentence:
        if letter != result[-1]:
            result.append(letter)
    print(result)
