from biblio import *

notas = entrada()
mediaNotas = media(notas)
resultados = conceito(notas)

saida(resultados, notas, mediaNotas)