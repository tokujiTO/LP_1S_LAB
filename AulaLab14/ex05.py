from random import uniform
acertos = 0
num = int(input("Digite o total de testes: "))
for c in range (1, num+1):
    y = uniform(-1, 1)
    x = uniform(-1, 1)
    n = x, y
    if x**2+y**2<=1:
        acertos += 1
pi = 4*acertos/num
print(f"π aproximadamente igual à {pi}")