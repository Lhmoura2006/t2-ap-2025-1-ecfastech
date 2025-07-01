votos = [0, 0, 0]
total = int(input("Total de eleitores: "))
for _ in range(total):
    voto = int(input("Vote no candidato 1, 2 ou 3: "))
    if voto in [1, 2, 3]:
        votos[voto-1] += 1
print(f"Candidato 1: {votos[0]} votos\nCandidato 2: {votos[1]} votos\nCandidato 3: {votos[2]} votos")
