while True:
    nome = input("Nome do atleta (Enter para sair): ")
    if nome == '':
        break
    saltos = []
    for i in range(5):
        salto = float(input(f"Salto {i+1}: "))
        saltos.append(salto)
    melhor = max(saltos)
    pior = min(saltos)
    media = (sum(saltos) - melhor - pior) / 3
    print(f"Melhor salto: {melhor} m")
    print(f"Pior salto: {pior} m")
    print(f"Média dos demais saltos: {media:.2f} m")
    print(f"Resultado final: {nome}: {media:.2f} m")
