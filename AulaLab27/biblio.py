def converte_moeda(danos):
    newlist = []
    for c in danos:
        if not c == 'Damages not recorded':
            if c[-1] == 'B':
                c = float(c[:-1]) * 1000000
                newlist.append(c)
            elif c[-1] == 'M':
                c = float(c[:-1]) * 1000
                newlist.append(c)
        else:
            newlist.append("Damages not recorded")
    return newlist


def gera_dic_nomes(nomes, meses, anos, max_velocidades, areas_aferadas, danos, mortes):
    dic_nomes = {}
    for i in range(len(nomes)):
        dic_nomes[nomes[i]] = [meses[i], anos[i], max_velocidades[i], areas_aferadas[i], danos[i], mortes[i]]
    return dic_nomes


def gera_dic_anos(nomes, meses, anos, max_velocidades, areas_aferadas, danos, mortes):
    dic_anos = {}
    for i in range(len(anos)):
        if anos[i] not in dic_anos:
            dic_anos[anos[i]] = [nomes[i], meses[i], max_velocidades[i], areas_aferadas[i], danos[i], mortes[i]]
        if anos[i] in dic_anos:
            dic_anos[anos[i]].append([nomes[i], meses[i], max_velocidades[i], areas_aferadas[i], danos[i], mortes[i]])
    return dic_anos

def contagem_areas(areas):
    cidades = {}
    for c in areas:
        for v in c:
            if v not in cidades:
                cidades[v] = 1
            elif v in cidades:
                cidades[v] = cidades[v] + 1
    return cidades
            