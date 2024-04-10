from math import sqrt
a = int(input('Digite o comprimento do 1º lado: '))
b = int(input('Digite o comprimento do 2º lado: '))
c = int(input('Digite o comprimento do 3º lado: '))
s = (a + b + c) / 2
K = sqrt(s*(s-a)*(s-b)*(s-c))
print(K)
