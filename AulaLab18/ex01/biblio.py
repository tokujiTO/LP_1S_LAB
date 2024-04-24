from random import randint
from collections import namedtuple

def gerar_votos(num):
    votos = list()
    for c in range(0, num):
        votos.append(randint(0,1))
    return votos

def concordancia(l1, l2):
    conc = 0
    if len(l1) != len(l2):
        return print("Erro! as listas n tem msm tamanho")
    else:
        for c, l in zip(l1, l2):
            if c > 1 or l > 1:
                return print("Erro! as listas só pode ter números 1 ou 0")
            elif c == l:
                conc += 1
        return conc
    
def gera_ficha_votos(nomes, num_votos):
    Ficha = namedtuple('Ficha', 'nome votacao')
    congressistas = []
    if len(nomes) > 1:
        for c in nomes:
            congressistas.append(Ficha(c, gerar_votos(num_votos)))
        return congressistas
    else:
        congressistas.append(Ficha(nomes, gerar_votos(num_votos)))
        return congressistas
    
# def busca_aliados(minha_ficha, fichas):
#     compatibilidade = []
#     for c in fichas:
#         cont = concordancia(minha_ficha[0].votacao, c.votacao)
#         compatibilidade.append(cont)
#     return compatibilidade

def meu_aliado(minha_ficha, fichas):
    melhor = ''
    score = count = 0
    for c in fichas:
        if concordancia(minha_ficha[0].votacao, c.votacao) > count:
            melhor = c.nome
            count = score = concordancia(minha_ficha[0].votacao, c.votacao)
    return [melhor, score]
        

    