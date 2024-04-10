from turtle import *
import turtle
# Constantes
LADO = 150            # Lado da "janela" (canvas)
VELOCIDADE = 7        # Escala de 1 a 13

# Criação do canvas
clearscreen()             # Limpa a tela da execução anterior
setup(2*LADO, 2*LADO)     # Tamanho da janela
bgcolor('lightgray')      # Cor de fundo da tela


# Criação da tartaruga donatelo
donatelo = Turtle()         # Criação
donatelo.speed(VELOCIDADE)  # Alterando a velocidade

##### INSIRA O SEU CÓDIGO #####

donatelo.forward(150*2**0.5)
donatelo.left(135)
donatelo.forward(150)
donatelo.left(90)
donatelo.forward(150)

turtle.done()