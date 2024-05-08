from biblio import *

#EX 1
carro = {"marca": "Ford", "modelo": "Mustang", "ano": 1964}

#a)
print(carro["modelo"])

#b)
carro.update({"cor" : "Vermelho"})
print(carro)

#c)
carro.pop("modelo")
print(carro)

#d)
for c in carro.items():
    print(c)

#EX 2
dic = {'a': 10, 'b': 7, 'c': 'vazio'}
lista = list(dic.keys())
print(lista)

#EX 3
dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(chave_presente(dic, 5))
print(chave_presente(dic, 9))

#EX 4
dic = {'e1': 10, 'e2': 20, 'e3': 6}
print(multiplica5(dic))

#EX 5
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d3 = {}
d3.update(d1)
d3.update(d2)
print(d3)

#EX 6 
dic = {'a': 12, 'b': 20, 'c': 12, 'd': 40}
print(removeDupl(dic))

#EX 7
soma = 0
dic = {'a': 2, 'b': 3 }
for c in dic.values():
    soma += c
print(soma)

#EX 8
dic = {}
for c in range(1,16):
    dic[c] = c**2
print(dic)

#EX 9
dic = {1: "um",2: "dois",3: "três",4: "quatro",6: "seis",9: "nove", 10: "dez"}
lista = []
for c in dic.keys():
    if c%3 == 0:
        lista.append(c)
for l in lista:
    dic.pop(l)
print(dic)

#EX 10
dic = {'M1' : [67,79,90,73,36], 'M2': [89,67,84], 'M3': [82,57] }
soma = 0
for c in dic.values():
    soma += len(c)
print(soma)