import re 

def subst(pattern, replace, string):
    return re.sub(pattern, replace, string)

if __name__ == '__main__':
    strings = ['JHONNY WAS HERE','JHON WAS WITH JHONNY', 'JHON JHONNY WAS HERE', 'JOHNNY AND JHON']
    pattern = re.compile(r'\bJHON\b')
    news = [subst(pattern, 'LUKAS', string) for string in strings]
    print(news)