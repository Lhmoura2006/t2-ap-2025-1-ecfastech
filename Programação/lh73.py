def filtrar_numeros(lista, tipo):
    if tipo == 'pares':
        return [n for n in lista if n % 2 == 0]
    elif tipo == 'impares':
        return [n for n in lista if n % 2 != 0]
    elif tipo == 'positivos':
        return [n for n in lista if n > 0]
    elif tipo == 'negativos':
        return [n for n in lista if n < 0]
    else:
        return []
