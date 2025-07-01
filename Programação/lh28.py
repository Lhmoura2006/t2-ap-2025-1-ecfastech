qtd_cds = int(input("Quantidade de CDs: "))
total = 0
for i in range(qtd_cds):
    preco = float(input(f"Preço do CD {i+1}: "))
    total += preco
print(f"Total investido: R$ {total:.2f}")
print(f"Valor médio por CD: R$ {total / qtd_cds:.2f}")
