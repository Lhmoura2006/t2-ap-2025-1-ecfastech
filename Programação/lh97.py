def validar_numeros_base(lista_de_strings, base):
    validos = []
    for s in lista_de_strings:
        s = s.upper()
        if s and all(c in DIGITOS[:base] for c in s):
            validos.append(s)
    return validos
