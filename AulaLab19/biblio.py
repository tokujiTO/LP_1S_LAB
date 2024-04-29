def gera_login(nome, sobrenome, ra):
    if len(nome) < 3:
        primeiraParte = (nome + sobrenome)[:3]
    else:
        primeiraParte = nome[:3]

    if len(sobrenome) < 3:
        segundaParte = sobrenome
    else:
        segundaParte = sobrenome[:3]

    if len(ra) < 3:
        terceiraParte = ra
    else:
        terceiraParte = ra[-3:]

    username = primeiraParte+segundaParte+terceiraParte
    
    return username.upper()

def valida_senha(senha):
    if len(senha)>=7 and not senha.islower() and not senha.isupper() and not senha.isalpha():
        return True
    else:
        return False

def conta_vogais(frase):
    vogais = 'aiueo'
    contagem = 0
    for c in frase.lower():
        if c in vogais:
            contagem += 1
    return contagem

def conta_consoantes(frase):
    contagem = 0
    vogais = 'aiueo'
    numeros = '1234567890'
    for c in frase.lower():
        if c not in vogais and c not in numeros and c not in ' ':
            contagem += 1

def pig_latim(frase):
    portuguesPorco = ''
    fatia = frase.split(" ")
    for c in fatia:
        palavra = ''
        palavra = c.lower()[1:] + c.lower()[0] + 'ay' + ' '
        portuguesPorco += palavra
    return portuguesPorco

def verficia_barras(data):
    if data[2] not in '/' and data[5] not in '/':
        return False
    else:
        return True
    
def verifica_campos(data):
    numeros = data.split('/')
    for c in numeros:
        if c.isalpha():
            validade = True
        else:
            return False
    return validade

def maximo(sequencia):
    maior = 0
    for c in sequencia:
        if int(c) >= len(sequencia)-3:
            maior = maior
        elif int(c)*int(c+1)*int(c*2) > maior:
            maior = int(c)*int(c+1)*int(c*2)
            
    return maior, 