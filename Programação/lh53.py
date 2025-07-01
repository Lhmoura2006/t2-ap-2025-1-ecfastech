def exercicio_53(matriz, elemento):
    count = sum(row.count(elemento) for row in matriz)
    print(f"Elemento {elemento} aparece {count} vezes.")
