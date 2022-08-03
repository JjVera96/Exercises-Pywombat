# https://pywombat.com/my/exercises/aaee3b26 

def unity_to_MB(value, unity):
    if unity == 'GB': value = value * 1024
    if unity == 'KB': value = value / 1024
    return value

if __name__ == '__main__':
    input_size = input('Tamaño: ')
    input_speed = input('Velocidad: ')

    size, size_unity = input_size.split(' ')
    speed, speed_unity = input_speed.split(' ')

    size = unity_to_MB(float(size), size_unity)
    speed = unity_to_MB(float(speed), speed_unity) / 8

    time = size/speed

    print('{} horas !!'.format(round(time/3600,2)))
    print('{} minutos !!'.format(round(time/60,2)))
    print('{} segundos !!'.format(round(time,2)))
