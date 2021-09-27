if __name__ == '__main__':
    numbers = [10, 35, -5, 14, 6, 12, -80, -7, -1, 23, 12, 13, -10]
    positive_numbers = list(filter(lambda x: x > 0, numbers))
    print(positive_numbers)
