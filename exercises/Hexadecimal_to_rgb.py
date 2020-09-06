hexa = input('Hexadecimal To Rgb: ')
hexa = hexa.lstrip('#')
rgb = tuple(int(hexa[i:i+2], 16) for i in (0, 2, 4))
print(rgb)