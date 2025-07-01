num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

inicio = min(num1, num2) + 1
fim = max(num1, num2)

for i in range(inicio, fim):
    print(i, end=' ')
