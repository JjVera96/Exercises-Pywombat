def ubbi_dubbi(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    ub_word = word
    for vowel in vowels:
        if vowel in word:
            ub_word = ub_word.replace(vowel, 'ub'+vowel)
    return ub_word

print(ubbi_dubbi('program'))
print(ubbi_dubbi('demo'))
print(ubbi_dubbi('car'))