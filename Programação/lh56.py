def exercicio_56(linhas, colunas):
    matriz = [[i*j for j in range(colunas)] for i in range(linhas)]
    for linha in matriz:
        print(linha)
