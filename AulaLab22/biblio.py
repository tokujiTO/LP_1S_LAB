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

# def calcula_medias():