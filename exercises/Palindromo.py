def palindromo(sentencia):
    sentencia = sentencia.lower().replace(' ', '')
    inverso_sentencia = ''.join(reversed(sentencia))
    print(True) if sentencia == inverso_sentencia else print(False)

palindromo('Anita lava la tina')
palindromo('Sometamos o matemos')
palindromo('Super palindromo')
