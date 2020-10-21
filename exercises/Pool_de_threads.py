from concurrent.futures import ThreadPoolExecutor

def fibonacci(number):
    if number <= 1:
        return number
    return(fibonacci(number-1) + fibonacci(number-2))

def task_fibbonacci(number):
    print('Resultado fib({}) = {}'.format(number, fibonacci(number)))

if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=4)
    for i in range(1, 31):
        executor.submit(task_fibbonacci(i))
    executor.shutdown()
