from random import randint

def sorteio(lados):
    result = randint(1, lados)
    return result

def multiplos_sorteios(numDados, numLados):
    resultados = []
    for c in range(numDados):
        resultados.append(sorteio(numLados))
    return resultados

def soma_quadrados(n):
    if n > 0:
        return n**2 + (soma_quadrados(n-1))
    else:
        return 0
    
def adiciona_contato(agenda, nome, tele, insta):
    contato = [tele, insta]
    agenda[f"{nome}"] = contato
    return agenda

def apaga_contato(agenda, nome):
    del agenda[nome]
    return agenda

def encontra_contato(agenda, nome):
    if nome in agenda:
        print(agenda[nome])
        return True
    else:
        print("O contato n está na agenda")
        return False
    
def atualiza_contato(agenda, nome):
    result = encontra_contato(agenda, nome)
    if result == True:
        print("Qual deseja alterar?\n[1] Celular\n[2] Instagram")
        opt = int(input("Digite a opção: "))
        while not 1 <= opt <= 2:
            print("OPÇÃO INVÁLIDA!")
            print("Qual deseja alterar?\n[1] Celular\n[2] Instagram")
            opt = int(input("Digite a opção: "))
        match opt:
            case 1:
                mudanca = input("Digite o novo celular: ")
                novo = [mudanca, agenda[nome][1]]
                agenda[nome] = novo
            case 2:
                mudanca = input("Digite o novo instagram: ")
                novo = [agenda[nome][0], mudanca]
                agenda[nome] = novo
        return agenda
    else:
        return None 

    