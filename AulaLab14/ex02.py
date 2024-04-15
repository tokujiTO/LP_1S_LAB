#ex 2
from time import time
divisores = list()
startTime = time()
while True:
    try:
        num = int(input("Digite um número: "))
        break
    except:
        print("vc digitou um número inválido!")
for c in range (1, (num//2)+1):
    if num % c == 0:
        divisores.append(c)
divisores.append(num)
finishTime = time()
print(divisores)

print(f"{finishTime - startTime :.2f} segundos")