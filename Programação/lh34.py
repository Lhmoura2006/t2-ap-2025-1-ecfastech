num = int(input("Digite um número inteiro: "))
if num > 1 and all(num % i != 0 for i in range(2, num)):
    print("Número primo.")
else:
    print("Não é primo.")

# 35) Lista de números primos até N
N = int(input("Mostrar primos até: "))
for num in range(2, N + 1):
    if all(num % i != 0 for i in range(2, num)):
        print(num, end=' ')
print()
