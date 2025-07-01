n = int(input("Quantos números vai digitar? "))
numeros = [int(input("Número: ")) for _ in range(n)]
print("Menor:", min(numeros), "Maior:", max(numeros), "Soma:", sum(numeros))
