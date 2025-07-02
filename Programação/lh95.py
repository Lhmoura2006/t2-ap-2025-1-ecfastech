DIGITOS = '0123456789ABCDEF'

def para_decimal(numero_str, base_origem):
    numero_str = numero_str.upper()
    valor = 0
    for i, c in enumerate(reversed(numero_str)):
        if c not in DIGITOS[:base_origem]:
            raise ValueError(f"Caractere inválido '{c}' para base {base_origem}")
        valor += DIGITOS.index(c) * (base_origem ** i)
    return valor

def de_decimal(decimal, base_destino):
    if decimal == 0:
        return '0'
    resultado = []
    while decimal > 0:
        resultado.append(DIGITOS[decimal % base_destino])
        decimal //= base_destino
    return ''.join(reversed(resultado))

def converter_base(numero_str, base_origem, base_destino):
    decimal = para_decimal(numero_str, base_origem)
    return de_decimal(decimal, base_destino)
