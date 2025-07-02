def encontrar_palindromos_base(lista_numeros_decimais, base):
    palindromos = []
    for n in lista_numeros_decimais:
        representacao = de_decimal(n, base)
        if representacao == representacao[::-1]:
            palindromos.append(n)
    return palindromos
