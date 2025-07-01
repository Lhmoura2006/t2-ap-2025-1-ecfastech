n = int(input("Quantas notas? "))
notas = [float(input("Nota: ")) for _ in range(n)]
print("Média:", sum(notas)/n)

# 25) Média de idades e classificação
n = int(input("Quantas pessoas? "))
idades = [int(input("Idade: ")) for _ in range(n)]
media = sum(idades)/n
if media <= 25:
    print("Turma jovem")
elif media <= 60:
    print("Turma adulta")
else:
    print("Turma idosa")
