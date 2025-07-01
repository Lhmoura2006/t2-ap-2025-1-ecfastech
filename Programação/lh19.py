n = int(input("Quantos números (entre 0 e 1000)? "))
numeros = []
for _ in range(n):
    while True:
        num = int(input("Número: "))
        if 0 <= num <= 1000:
            numeros.append(num)
            break
print("Menor:", min(numeros), "Maior:", max(numeros), "Soma:", sum(numeros))
