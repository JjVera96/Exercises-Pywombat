l = []

while(len(l) < 3):
    if(len(l)== 0): posicion = 'primer'
    if(len(l)== 1): posicion = 'segundo'
    if(len(l)== 2): posicion = 'tercer'
    num = input('Ingresa tu {} número: '.format(posicion))
    l.append(num) if int(num) > 0 else print('El número debe ser positivo')
        
l.sort(reverse=True)
print(l[0], l[1], l[2])