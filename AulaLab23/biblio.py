from random import choice

def criar_baralho():
    baralho = []
    for naipe in range(1, 5):
        match naipe:
            case 1:
                naipe = "Ouro"
            case 2:
                naipe = "Espadas"
            case 3:
                naipe = "Copas"
            case 4:
                naipe = "Paus"
        for c in range(1, 14):
            carta = {}
            if c > 10:
                match c:
                    case 11:
                        c = "J"
                    case 12:
                        c = "Q"
                    case 13:
                        c = "K"
            carta[naipe] = c
            baralho.append(carta)
    return baralho

def distribuir_cartas(baralho, cada):
    mao = []
    for c in range(int(cada)):
        carta = choice(baralho) 
        mao.append(carta)
        baralho.pop(baralho.index(carta))
    return mao

