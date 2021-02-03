import re 

string = 'Pywombat, Article, Regex; Videos; Tutorials: Resources; AWS'
regex = re.compile(r", |; |: ")
results = regex.split(string)
print(results)