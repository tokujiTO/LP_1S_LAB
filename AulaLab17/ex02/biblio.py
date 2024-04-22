def entrada():
    notas = list()
    for c in range(0, 5):
        nota = int(input("Digite uma nota: "))
        while nota<0 or nota> 100:
            print("Erro! nota inválida")
            nota = int(input("Digite a nota: "))
        notas.append(nota)
    return notas

def media(notas):
    media = sum(notas)/len(notas)
    return media

def conceito(notas):
    conceitos = list()
    for c in range(0, len(notas)):
        if notas[c] < 60:
            conceitos.append("F")
        elif notas[c] < 70:
            conceitos.append("D")
        elif notas[c] < 80:
            conceitos.append("C")
        elif notas[c] < 90:
            conceitos.append("B")
        else:
            conceitos.append("A")
    return conceitos

def saida(resultados, notas, mediaNotas):
    print(f"A media do grupo foi {mediaNotas}")
    resultado = zip(notas, resultados)
    for nota, conceito in resultado:
        print(f"{nota} => {conceito}")