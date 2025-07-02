def somar_em_bases(lista_numeros, base_origem, base_destino):
    soma_decimal = 0
    for num in lista_numeros:
        try:
            soma_decimal += para_decimal(num, base_origem)
        except ValueError:
            print(f"Erro: '{num}' não é válido para base {base_origem}")
    return de_decimal(soma_decimal, base_destino)
