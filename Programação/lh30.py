preco_pao = float(input("Preço do pão: R$ "))
print("Panificadora Pão de Ontem - Tabela de preços")
for i in range(1, 51):
    print(f"{i} - R$ {preco_pao * i:.2f}")
