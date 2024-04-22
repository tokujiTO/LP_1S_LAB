import entrada
import saida
from math import ceil

area, preco = entrada.entrada()

galoes = ceil(area / 112)
horas = ceil(8*(area / 112))
custoRelativo = galoes*preco
taxa = horas * 35
custoTotal = taxa + custoRelativo

saida.saida(galoes, horas, custoRelativo, taxa, custoTotal)
