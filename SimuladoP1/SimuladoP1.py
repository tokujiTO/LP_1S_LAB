
#1 - 
p1 = float(input("Digite a nota da P1: "))
p2 = float(input("Digite a nota da P2: "))
t1 = float(input("Digite a nota da T1: "))
t2 = float(input("Digite a nota da T2: "))
t3 = float(input("Digite a nota da T3: "))

mp = (p1 + p2)/2
mt = 0.4*t1 + 0.4*t2 + 0.2*t3
mf = (mp+mt)/2
if mf >= 6:
	print("Aprovado")
else: 
	print("Reprovado")




#3 -
valor = int(input("Digite um número inteiro e par: "))
while valor <= 0 or valor % 2 != 0:
	print("vALOR INVÁLIDO")
	valor = int(input("Digite um número inteiro e par: "))

quantidadeDeNotasDe100 = valor//100
valor = valor - (quantidadeDeNotasDe100*100)

quantidadeDeNotasDe50 = valor//50
valor = valor - (quantidadeDeNotasDe50*50)

quantidadeDeNotasDe20 = valor//20
valor = valor - (quantidadeDeNotasDe20*20)

quantidadeDeNotasDe10 = valor//10
valor = valor - (quantidadeDeNotasDe10*10)

quantidadeDeNotasDe5 = valor//5
valor = valor - (quantidadeDeNotasDe5*5)

quantidadeDeNotasDe2 = valor//2

print(f"A quantidade de notas de 100 recolhidas foi {quantidadeDeNotasDe100}\nA quantidade de notas de 50 recolhidas foi {quantidadeDeNotasDe50}\nA quantidade de notas de 20 recolhidas foi {quantidadeDeNotasDe20}\nA quantidade de notas de 10 recolhidas foi {quantidadeDeNotasDe10}\nA quantidade de notas de 5 recolhidas foi {quantidadeDeNotasDe5}\nA quantidade de notas de 2 recolhidas foi {quantidadeDeNotasDe2}\n")


# 4 - 
numero = int(input("Digite um número: "))
count = 0
for c in range(2, numero):
	if numero % c == 0:
		count += 1
if numero >2:
	if count > 0:
		print("O número não é primo")
	else:
		print("O número é primo") 
else:
	if numero == 2:
		print("O numero é primo")
	else:
		print("O numero não é primo")