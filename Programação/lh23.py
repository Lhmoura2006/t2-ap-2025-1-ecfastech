N = int(input("Digite N: "))
cont = 0
for num in range(2, N+1):
    primo = True
    for i in range(2, num):
        cont += 1
        if num % i == 0:
            primo = False
            break
    if primo:
        print(num, end=' ')
print("\nDivisões realizadas:", cont)
