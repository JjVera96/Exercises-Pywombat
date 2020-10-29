file_name = input("Ingresa la dirección del archivo: ")

try:
    with open(file_name, 'r') as file:
        print(file.read())
except:
    print("No fue posible obtener el archivo")