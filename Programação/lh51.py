def exercicio_51(n):
    soma = 0
    for i in range(1, n+1):
        denominador = 2*i - 1
        soma += i / denominador
        print(f"{i}/{denominador}", end=" + " if i < n else " = ")
    print(f"{soma:.4f}")
