from random import randint

def jogador():
    print("-=-"*20)
    print('Faça uma decisão: \n[0]Pedra\n[1]Papel\n[2]Teoura')
    escolhaPlayer = int(input("Sua escolha: "))
    return escolhaPlayer

def computador():
    escolhaPC = randint(0, 3)
    return escolhaPC

def quem_ganhou(x,y, cond):
    print("-=-"*20)
    if x == 2 and y == 1:
        print("Jogador venceu!")
        cond = False
    elif x == 1 and y == 0:
        print("Jogador venceu!")
        cond = False
    elif x == 0 and y == 2:
        print("Jogador venceu!")
        cond = False
    elif y == 2 and x == 1:
        print("Computador venceu!")
        cond = False
    elif y == 1 and x == 0:
        print("Computador venceu!")
        cond = False
    elif y == 0 and x == 2:
        print("Computador venceu!")
        cond = False
    else:
        print("EMPATE!")
        cond = True
    return()
