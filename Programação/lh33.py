temperaturas = []
while True:
    temp = input("Digite a temperatura (ou ENTER para sair): ")
    if temp == '':
        break
    temperaturas.append(float(temp))
if temperaturas:
    print(f"Menor: {min(temperaturas)}")
    print(f"Maior: {max(temperaturas)}")
    print(f"Média: {sum(temperaturas)/len(temperaturas):.2f}")
else:
    print("Nenhuma temperatura informada.")
