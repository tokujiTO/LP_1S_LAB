import turtle
from turtle import *
import math

# Constantes
LADO = 150            # Lado da "janela" (canvas)
VELOCIDADE = 4        # Escala de 1 a 13

# Criação do canvas
clearscreen()             # Limpa a tela da execução anterior
setup(8*LADO, 4*LADO)     # Tamanho da janela
bgcolor('purple')      # Cor de fundo da tela          

# Criação da tartaruga donatelo
donatelo = Turtle()         # Criação
donatelo.speed(VELOCIDADE)
donatelo.color('white')  # Alterando a velocidade
donatelo.shape('turtle')

# Movimentação
donatelo.begin_fill()
donatelo.right(45)       # donatelo.fd(100)
donatelo.forward(150)
donatelo.right(135)
donatelo.forward((2*(150**2))**0.5)
donatelo.right(135)
donatelo.forward(150)
donatelo.end_fill()
donatelo.right(90)
donatelo.forward(150)
donatelo.left(165)
donatelo.forward(2*((2*(150**2))**0.5)/2)
donatelo.left(120)
donatelo.forward(2*((2*(150**2))**0.5)/2)

turtle.done()