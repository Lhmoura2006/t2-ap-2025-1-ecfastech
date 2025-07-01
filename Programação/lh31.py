while True:
    total = 0
    produto = 1
    print("Lojas Tabajara")
    while True:
        preco = float(input(f"Produto {produto}: R$ "))
        if preco == 0:
            break
        total += preco
        produto += 1
    print(f"Total: R$ {total:.2f}")
    dinheiro = float(input("Dinheiro: R$ "))
    print(f"Troco: R$ {dinheiro - total:.2f}")
    continuar = input("Nova compra? (s/n) ").lower()
    if continuar != 's':
        break
