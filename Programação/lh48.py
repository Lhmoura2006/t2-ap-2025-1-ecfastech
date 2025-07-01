num = int(input("Número inteiro positivo: "))
invertido = 0
temp = num
while temp > 0:
    invertido = invertido * 10 + temp % 10
    temp //= 10
print(f"Número invertido: {invertido}")
