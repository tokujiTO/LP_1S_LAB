lista = list()
maior = menor = 0
for c in range(0,5):
    lista.append(int(input("Digite um número:")))
    if c == 0:
        maior = menor = lista[0]
    elif lista[c] > maior:
        maior = lista[c]
    elif lista[c] < menor:
        menor = lista[c]
print(f"O maior número digitado foi {maior} na posição {lista.index(maior)} e o menor foi {menor} na posição {lista.index(menor)}")