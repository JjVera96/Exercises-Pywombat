from Factorial import factorial_iterativo

def combinatoria(n, k):
    fact_n = factorial_iterativo(n)
    fact_k = factorial_iterativo(k)
    fact_nk = factorial_iterativo(n-k)
    return fact_n // (fact_k*fact_nk)

print(combinatoria(8,2))