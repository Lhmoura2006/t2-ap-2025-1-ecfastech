def exercicio_55(matriz):
    elementos = [item for row in matriz for item in row]
    print(f"Maior elemento: {max(elementos)}")
    print(f"Menor elemento: {min(elementos)}")
