gabarito = ['A','B','C','D','E','E','D','C','B','A']
acertos_alunos = []
while True:
    acertos = 0
    for i in range(10):
        resposta = input(f"Resposta questão {i+1}: ").upper()
        if resposta == gabarito[i]:
            acertos += 1
    acertos_alunos.append(acertos)
    if input("Outro aluno? (s/n): ").lower() != 's':
        break
print(f"Maior acerto: {max(acertos_alunos)}")
print(f"Menor acerto: {min(acertos_alunos)}")
print(f"Total de alunos: {len(acertos_alunos)}")
print(f"Média da turma: {sum(acertos_alunos)/len(acertos_alunos):.2f}")
