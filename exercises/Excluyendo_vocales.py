from string import ascii_lowercase

def excludes_vowel_counter(stg):
    stg = stg.lower()
    letters = list(set(ascii_lowercase) - set('aeiou'))
    return sum([stg.count(_) for _ in letters])

print(excludes_vowel_counter('Hola mundo'))
print(excludes_vowel_counter('Eduardo Ismael'))
print(excludes_vowel_counter('PyWombat'))
    