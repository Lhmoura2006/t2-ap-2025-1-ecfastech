num = int(input("Digite um número: "))
divisores = [i for i in range(2, num) if num % i == 0]
if not divisores:
    print("É primo.")
else:
    print("Não é primo. Divisores:", divisores)
