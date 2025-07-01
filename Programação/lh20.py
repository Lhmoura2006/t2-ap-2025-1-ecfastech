while True:
    n = int(input("Número para fatorial (0-15): "))
    if 0 <= n < 16:
        fat = 1
        for i in range(n, 0, -1):
            fat *= i
        print(f"{n}! = {fat}")
    else:
        print("Número inválido.")
    if input("Deseja continuar? (s/n): ") != 's':
        break
