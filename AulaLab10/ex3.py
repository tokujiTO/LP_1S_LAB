base = int(input("Digite o valor inicial do crescimento populacional: "))
indice = int(input("Digite o expoente q o numero será elevado(ritmo de crescimento): "))
limit = int(input("Digite o limite populacional: "))
while base <= limit:
    base = base**indice
    print(base)
    