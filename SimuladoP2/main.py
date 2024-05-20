from biblio import *

# 1 A
print(sorteio(8))

# 1 B
print(multiplos_sorteios(5, 15))

# 1 C
lados = int(input("Digite o numero de lados q deve ser maior que 3: "))
while lados < 3:
    print("ERRO! O NUMERO DE LADOS DEVE SER MAIOR Q 3")
    lados = int(input("Digite o numero de lados q deve ser maior q 3: "))
numDados = int(input("Digite o numero de lados q devem ser lançados: "))
resultado = multiplos_sorteios(numDados, lados)
print(resultado)
print(sum(resultado))

# 2 A
print(soma_quadrados(5))

# 2 B
n = int(input("Digite os n termos: "))
while n < 0:
    print("ERRO, O NUMERO DEVE SER INTEIRO E POSITIVO")
    n = int(input("Digite os n termos: "))
print(soma_quadrados(n))

# 3 
agenda = {'Gustavo Alves': ['(11) 99685-2345', '@gu_alves'],
          'Laura Alves': ['(11) 97428-2001', '@lalinha_alves'],
          'Janaina Goulart': ['(21) 92134-0543', '@jango_25'],
          'Maria Prado': ['(35) 93821-2289', '@mariaprado_insta'],
          'Zenon Galhardo': ['(13) 92121-3997', '@zengalhardo']}

# A)
nome = "Joaquim Santos"
cel = "(13) 94576=1209"
insta = "@jocantos"
nova_agenda = adiciona_contato(agenda, nome, cel, insta)
print(nova_agenda)

# B)
apaga_contato(agenda, 'Maria Prado')
print(agenda)

# C)
# Teste da função encontra_contato
encontra_contato(agenda, 'Laura Alves')
encontra_contato(agenda, 'Cleber Silva')

# D)
atualiza_contato(agenda, 'Laura Alves')
atualiza_contato(agenda, 'Cleber Silva')
print(agenda)