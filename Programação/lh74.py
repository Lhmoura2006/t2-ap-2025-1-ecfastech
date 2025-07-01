def calcular_fatorial_iterativo(numero):
    if numero < 0:
        return "Erro: número negativo"
    fat = 1
    for i in range(2, numero+1):
        fat *= i
    return fat

def calcular_fatorial_recursivo(numero):
    if numero < 0:
        return "Erro: número negativo"
    if numero == 0 or numero == 1:
        return 1
    return numero * calcular_fatorial_recursivo(numero - 1)
