N = int(input("Mostrar primos até: "))
for num in range(2, N + 1):
    if all(num % i != 0 for i in range(2, num)):
        print(num, end=' ')
print()
