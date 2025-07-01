votos = {1:0,2:0,3:0,4:0,5:0,6:0}
while True:
    voto = int(input("Voto (0 para fim): "))
    if voto == 0:
        break
    if voto in votos:
        votos[voto] += 1
total_votos = sum(votos.values())
print(f"Votos candidato 1: {votos[1]}")
print(f"Votos candidato 2: {votos[2]}")
print(f"Votos candidato 3: {votos[3]}")
print(f"Votos candidato 4: {votos[4]}")
print(f"Votos nulos: {votos[5]}")
print(f"Votos em branco: {votos[6]}")
print(f"% votos nulos: {(votos[5]/total_votos)*100:.2f}%")
print(f"% votos em branco: {(votos[6]/total_votos)*100:.2f}%")
