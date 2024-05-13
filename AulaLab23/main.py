from biblio import *

# EX 1
# A)
# print(criar_baralho())
# B)
# global baralho
# baralho = criar_baralho()
# valor_mao = distribuir_cartas(baralho, 4)
# print("\n Valo da mão: ", valor_mao)
# print(baralho)
# C)
global baralho
baralho = criar_baralho()
pessoas = int(input("Quantas pessoas vão jogar? "))
cartas_por_pessoas = len(baralho) / pessoas
print(len(baralho))
for c in range(pessoas):
    print(f"Jogador {c+1} = {distribuir_cartas(baralho, cartas_por_pessoas)}")

    
