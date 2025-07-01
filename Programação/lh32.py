n = int(input("Fatorial de: "))
fat = 1
fatores = []
for i in range(n, 0, -1):
    fat *= i
    fatores.append(str(i))
print(f"{n}! = {' . '.join(fatores)} = {fat}")
