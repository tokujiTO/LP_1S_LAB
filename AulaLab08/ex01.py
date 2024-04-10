import turtle
from turtle import *

# Constantes
LADO = 150            # Lado da "janela" (canvas)
VELOCIDADE = 4        # Escala de 1 a 13

# Criação do canvas
clearscreen()             # Limpa a tela da execução anterior
setup(2*LADO, 2*LADO)     # Tamanho da janela
bgcolor('purple')      # Cor de fundo da tela          

# Criação da tartaruga donatelo
donatelo = Turtle()         # Criação
donatelo.speed(VELOCIDADE)
donatelo.color('white')  # Alterando a velocidade

# Movimentação
donatelo.forward(100)       # donatelo.fd(100)
donatelo.left(90)           # donatelo.lt(45)
donatelo.forward(100)
donatelo.left(90)          # donatelo.rt(65)
donatelo.forward(100)      # donatelo.bk(150)
donatelo.left(90)
donatelo.forward(100)

turtle.done()