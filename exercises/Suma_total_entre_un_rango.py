def suma_cero_to_n(n):
    return int((n*(n+1))/2)

if __name__ == '__main__':

    start = int(input('Desde: '))
    end  = int(input('Hasta: '))

    if start > end: print('Error')
    else:    
        sum_start = suma_cero_to_n(abs(start))
        sum_end = suma_cero_to_n(abs(end))

        if start < 0: sum_start *= -1
        if end < 0: sum_end *= -1

        if start < 0 and end < 0:
            result = sum_start - sum_end + end 
        elif start < 0 and end > 0:
            result = sum_end + sum_start
        else: 
            result = sum_end - sum_start + start

        print(result)
