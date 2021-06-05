if __name__ == '__main__':
    n = input()
    while(len(str(n)) != 1):
        sum = 0
        for i in n:
            sum += int(i)
        n = str(sum)
    print(n)
    