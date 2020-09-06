calificaciones = [10, 10, 8, 7, 9]
alumnos = ['Eduardo', 'Fernando', 'Mariana', 'Raquel', 'Santiago']

for alum, cal in zip(alumnos, calificaciones):
    print('{} posee una calificación de: {}'.format(alum, cal))