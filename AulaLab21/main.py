from biblio import *

# EX 1
print(trocaLetras("Eu n tenho animais", "n", "t"))
print(qualPrimeiro("abelha", "alberto"))
print(somaTudo("2 9 10 29.5 23 43"))
lista = ["Tiago", "Pedro", "Lucas", "Gabriel"]
print(insereSeNovo("Tokugi", lista))
lista = ['Ronaldo', 'Romario', 'Rivelino']
pos = insereSeNovo('Romario', lista)
pos = insereSeNovo('Pele', lista)
pos = insereSeNovo('Rivelino', lista)
print(f'{lista}, que deve ser Ronaldo, Romario, Rivelino, Pele.')
escadaVertical("vanessa")

# EX 2
data = str(input("Digite a sua data de nascimento no modelo dd/mm/aaaa: "))
print(fazSenha(data))

# EX 3
dna = str(input("Digite uma cadeia de DNA pra pegar sua complementar:"))
print(dnaComplementar(dna))

# EX 4
titulos = """O Senhor dos Anéis
Harry Potter e a Pedra Filosofal
1984
O Lobo da Estepe
Cem Anos de Solidão
A Metamorfose
A Revolução dos Bichos
Crime e Castigo
Macunaíma"""
print(ordenaTitulos(titulos))

# EX 5
artigos = [
'RecurrentGPT: Interactive Generation of (Arbitrarily) Long Text',
'VideoLLM: Modeling Video Sequence with Large Language Models',
'Watermarking Text Data on Large Language Models for Dataset Copyright Protection',
'InheritSumm: A General, Versatile and Compact Summarizer by Distilling from GPT',
'Can Large Language Models emulate an inductive Thematic Analysis of semi-structured interviews? An exploration and provocation on the limits of the approach and the model',
'GPT-SW3: An Autoregressive Language Model for the Nordic Languages',
'The Emergence of Economic Rationality of GPT',
'Can We Edit Factual Knowledge by In-Context Learning?',
'G3Detector: General GPT-Generated Text Detector',
'GPT Paternity Test: GPT Generated Text Detection with GPT Genetic Inheritance'
]
print(contaPalavra("GPT", artigos))