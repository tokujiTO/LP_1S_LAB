def mult_rec(x, y):
    if x>0:
        return y + mult_rec(x-1, y)
    else:
        return 0

def imprime_astericos(n):
    # if n>0:
    #     return "*"*n+"\n"+imprime_astericos(n-1)
    # else:
    #     return ""
    if n == 0:
        return ""
    else:
        imprime_astericos(n-1)
        print("*"*n)

def max_valor(lista):
    if len(lista) > 1:
        lista.pop(lista.index(min(lista)))
        return max_valor(lista)
    else:
        return lista
    
def soma_lista(lista):
    if len(lista) > 0:
        return lista.pop() + soma_lista(lista)
    else:
        return 0
    

