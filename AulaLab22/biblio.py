def ordena_dic(dic):
    novoDicio = {}
    for c, v in dic.items():
        novoDicio[c] = sorted(v)
    return novoDicio

def mais_caros(dic):
    novoDic = {}
    maiores = {}
    novoDic = sorted(dic.values())
    maiores = novoDic[-3:]
    return maiores

def calcula_medias(lista):
    novaLista = []
    for d in lista:
        dicti = dict()
        dicti["RA"] = d["RA"]
        media = (d["P1"] + d["P2"])/2
        dicti["Media"] = media
        novaLista.append(dicti)
    return novaLista