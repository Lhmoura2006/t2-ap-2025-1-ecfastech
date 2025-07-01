precos = {100:1.20, 101:1.30, 102:1.50, 103:1.20, 104:1.30, 105:1.00}
total = 0
while True:
    codigo = int(input("Código do item (0 para sair): "))
    if codigo == 0:
        break
    if codigo in precos:
        qtd = int(input("Quantidade: "))
        valor = precos[codigo] * qtd
        total += valor
        print(f"Valor a pagar pelo item: R$ {valor:.2f}")
    else:
        print("Código inválido.")
print(f"Total do pedido: R$ {total:.2f}")
