vowel = 'aeiouAEIOU'

def pig_latin(string):
    words = string.split(" ")
    new_words = []
    for word in words:
        if string[0] in vowel:
            word = word + 'way'        
        else:
            word = word[1::] + word[0] + 'ay'
        new_words.append(word)
    return ' '.join(new_words)

print(pig_latin('Python'))
print(pig_latin('School'))
print(pig_latin('Hello World'))
print(pig_latin('air'))
print(pig_latin('eat'))