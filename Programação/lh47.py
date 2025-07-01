while True:
    nome = input("Nome do ginasta (Enter para sair): ")
    if nome == '':
        break
    notas = []
    for i in range(7):
        nota = float(input(f"Nota {i+1}: "))
        notas.append(nota)
    melhor = max(notas)
    pior = min(notas)
    media = (sum(notas) - melhor - pior) / 5
    print(f"Melhor nota: {melhor}")
    print(f"Pior nota: {pior}")
    print(f"Média: {media:.2f}")
