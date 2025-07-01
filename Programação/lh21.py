num = int(input("Digite um número: "))
if num > 1 and all(num % i != 0 for i in range(2, num)):
    print("É primo.")
else:
    print("Não é primo.")
