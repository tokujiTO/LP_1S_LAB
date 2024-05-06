def trocaLetras(frase, a, b):
    novaFrase = frase.replace(a, b)
    return novaFrase

def qualPrimeiro(p1, p2):
    try:
        if p1 < p2:
            return p1
        elif p2 < p1:
            return p2
    except:
        return "Não são comparáveis"

def somaTudo(linha):
    soma = 0
    for c in linha.split():
        soma += float(c)
    return soma

def insereSeNovo (nome, lista):
  ''' (str, list) -> int
  Modifica a lista, inserindo nome na lista.
  Retorna a posição de nome na lista ou None caso ele já exista.
  '''
  if nome in lista:
      return None
  else:
      lista.append(nome)
      posicao = lista.index(nome)
      return posicao
  
def escadaVertical(nome):
    for c in range(len(nome)):
        print(nome[:c+1].upper())

def fazSenha(data):
    senha = ""
    lista = data.split("/")
    senha = lista[1] + "$" + lista[0][::-1] + "#" + lista[0] + "!" + lista[1][::-1] + "\\" + lista[2]
    return senha

def dnaComplementar(dna):
    compl = ""
    for c in dna.upper():
        if c == "A":
            compl = compl + "T"
        elif c == "T":
            compl = compl + "A"
        elif c == "C":
            compl = compl + "G"
        elif c == "G":
            compl = compl + "C"
    return compl

def ordenaTitulos(lista):
    novaLista = lista.split("\n")
    novaLista.sort()
    return novaLista

def contaPalavra(nome, lista):
    count = 0
    for c in lista:
        count += c.count(nome)
    return count