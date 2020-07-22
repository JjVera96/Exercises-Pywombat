times = 0
listas = []
while times < 2:
    lista = []
    name = 'segunda' if times else 'primera'
    cant = int(input("Ingresa la longitud de la {} lista: ".format(name)))
    for i in range(cant):
        x = int(input("Ingresa un número a la lista: "))
        lista.append(x)
    listas.append(lista)
    times += 1
    
print(listas[0], listas[1])