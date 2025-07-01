turmas = int(input("Quantas turmas? "))
total_alunos = 0
for _ in range(turmas):
    while True:
        alunos = int(input("Alunos na turma: "))
        if alunos <= 40:
            total_alunos += alunos
            break
        print("Máximo de 40 alunos!")
print("Média de alunos por turma:", total_alunos/turmas)
