n = int(input("Número de termos: "))
soma = 0
for i in range(1, n+1):
    denominador = 2*i - 1
    soma += i / denominador
print(f"Soma da série: {soma:.4f}")
