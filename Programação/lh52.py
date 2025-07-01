def exercicio_52(matriz):
    n = len(matriz)
    soma_principal = sum(matriz[i][i] for i in range(n))
    soma_secundaria = sum(matriz[i][n - 1 - i] for i in range(n))
    print(f"Soma diagonal principal: {soma_principal}")
    print(f"Soma diagonal secundária: {soma_secundaria}")
