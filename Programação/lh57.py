def exercicio_57(matriz):
    linhas = len(matriz)
    colunas_iguais = all(len(row) == len(matriz[0]) for row in matriz)
    quadrada = linhas == len(matriz[0]) if colunas_iguais else False
    print(quadrada and colunas_iguais)
