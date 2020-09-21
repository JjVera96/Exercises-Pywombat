import time 

def execution_time(function):
    
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        print('Tiempo de ejecución: {} ms'.format(end_time-start_time))
        return result
    
    return wrapper

@execution_time
def super_task():
    import time

    time.sleep(1)
    return 10

super_task()
