import time

def total_time(function):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        print('Segundos transcurridos: {}s'.format(round(end_time-start_time)))
        return result

    return wrapper

@total_time
def suma(a, b):
    time.sleep(3)
    return a + b

suma(10,20)
