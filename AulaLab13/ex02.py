from math import log
soma = 0
x = int(input("Digite um número x: "))
n = int(input("Digite um número n: "))
while x < 0:
    print("NÚMEOR INVÁLIDO")
    x = int(input("Digite um número x: "))
while n < 0:
    print("NÚMEOR INVÁLIDO")
    x = int(input("Digite um número n: "))
for c in range(1, n):
    soma += ((x**c)/c)
soma = soma + log(x)
print(soma)