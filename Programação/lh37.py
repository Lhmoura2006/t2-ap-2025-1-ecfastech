clientes = []
while True:
    codigo = int(input("Código (0 para sair): "))
    if codigo == 0:
        break
    altura = float(input("Altura (m): "))
    peso = float(input("Peso (kg): "))
    clientes.append({"codigo": codigo, "altura": altura, "peso": peso})

if clientes:
    mais_alto = max(clientes, key=lambda c: c["altura"])
    mais_baixo = min(clientes, key=lambda c: c["altura"])
    mais_gordo = max(clientes, key=lambda c: c["peso"])
    mais_magro = min(clientes, key=lambda c: c["peso"])
    media_altura = sum(c["altura"] for c in clientes) / len(clientes)
    media_peso = sum(c["peso"] for c in clientes) / len(clientes)
    print(f"Mais alto: {mais_alto['codigo']} - {mais_alto['altura']}m")
    print(f"Mais baixo: {mais_baixo['codigo']} - {mais_baixo['altura']}m")
    print(f"Mais gordo: {mais_gordo['codigo']} - {mais_gordo['peso']}kg")
    print(f"Mais magro: {mais_magro['codigo']} - {mais_magro['peso']}kg")
    print(f"Média de altura: {media_altura:.2f}m")
    print(f"Média de peso: {media_peso:.2f}kg")
else:
    print("Nenhum cliente informado.")
