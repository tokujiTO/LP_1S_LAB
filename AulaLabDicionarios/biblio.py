def chave_presente(dic, val):
    for c in dic.keys():
        if c == val:
            return "A chave está presente na lista"
    return "A chave não está presente na lista"

def multiplica5(dic):
    nDic = {}
    for c, v in dic.items():
        nDic[c] = v*5
    return nDic

def removeDupl(dic):
    nDic = dic.copy()
    lista = list(dic.values())
    for c, v in dic.items():
        if lista.count(v)>=2:
            nDic.pop(c)
            lista.pop(lista.index(v))  
    return nDic
