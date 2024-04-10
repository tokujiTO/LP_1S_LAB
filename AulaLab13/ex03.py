from random import choice
candidatos = (-1, 0, 1, 2, 3)
votosTotais = []
n = int(input("digite quantos eleitores teremos: "))
for c in range(0, n):
    voto = choice(candidatos)
    votosTotais.append(voto)
print(f"Votos nulos = {votosTotais.count(-1)}")
print(f"Votos brancos = {votosTotais.count(0)}")
print(f"Votos candidato 1 = {votosTotais.count(1)}")
print(f"Votos candidato 2 = {votosTotais.count(2)}")
print(f"Votos candidato 3 = {votosTotais.count(3)}")
if votosTotais.count(1) == max(votosTotais.count(1), votosTotais.count(2), votosTotais.count(3)):
    vencedor = "candidato 1"
elif votosTotais.count(2) == max(votosTotais.count(1), votosTotais.count(2), votosTotais.count(3)):
    vencedor = "candidato 2"
else:
    vencedor = "candidato 3"
porcentagemVencedor = (max(votosTotais.count(1), votosTotais.count(2), votosTotais.count(3))/len(votosTotais))*100
print(f"O vencedor da votação foi o {vencedor}, com {porcentagemVencedor:.2f}% dos votos")
print(votosTotais)