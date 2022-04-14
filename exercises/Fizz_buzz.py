# https://pywombat.com/my/exercises/3a8fc8a8
# https://pywombat.com/my/exercises/3507deb0

if __name__ == '__main__':
    n = 100
    for i in range(n+1):
        x = ''
        if i % 3 == 0: x += 'fizz'
        if i % 5 == 0: x += 'buzz'
        print(x) if x != '' else print(i)
