from biblio import *
from collections import namedtuple

# votos1 = gerar_votos(5)
# print(votos1)
# votos2 = gerar_votos(5)
# print(votos2)
# conc = concordancia(votos1, votos2)
# print(f"A concordância dos candidatos 1 e 2 foi de {conc}")
numvotos = 10

nomes = ["Tiago", "Joao", "Enzo", "Pedro"]
fichas = gera_ficha_votos(nomes, numvotos)

eu = 'Tokugi'
minha_ficha = gera_ficha_votos([eu], numvotos)

print(meu_aliado(minha_ficha, fichas))
aliado, score = meu_aliado(minha_ficha, fichas)
print(f'O melhor aliado de {eu} é {aliado}, com alinhamento igual a {score}')

