#ex 3
from time import time
startTime = time()
divisores = list()
while True:
    try:
        num = int(input("Digite um número: "))
        break
    except:
        print("vc digitou um número inválido!")
for c in range (1, int((num**0.5)+1)):
    if num % c == 0:
        if num/c != c:
            divisores.append(int(num/c))
        divisores.append(c)
finishTime = time()
divisores.sort()
print(divisores)
print(f"{finishTime - startTime :.2f} segundos")