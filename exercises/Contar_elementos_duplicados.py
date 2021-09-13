if __name__ == '__main__':
    list = [1, 3, 4, 4, 5, 6, 1, 1, 4, 5, 10]
    result = []
    for num in list:
        if not num in result:
            result.append(num)

    print(result)
