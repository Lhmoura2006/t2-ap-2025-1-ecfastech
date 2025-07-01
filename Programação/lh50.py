N = int(input("Número de termos: "))
H = 0
for i in range(1, N+1):
    H += 1/i
print(f"Valor de H com {N} termos: {H:.4f}")
