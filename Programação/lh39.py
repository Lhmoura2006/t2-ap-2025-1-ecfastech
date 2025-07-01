alunos = []
for _ in range(10):
    num = int(input("Número do aluno: "))
    altura = float(input("Altura (cm): "))
    alunos.append({"num": num, "altura": altura})
mais_alto = max(alunos, key=lambda a: a["altura"])
mais_baixo = min(alunos, key=lambda a: a["altura"])
print(f"Aluno mais alto: {mais_alto['num']} com {mais_alto['altura']} cm")
print(f"Aluno mais baixo: {mais_baixo['num']} com {mais_baixo['altura']} cm")
