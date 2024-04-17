lista = [1, 2, 43, 23, 5, 34 ,543, 5432, 4, 3, 432, 2, 4, -5, -9]

imparesNegativos = [num for num in lista if num%2==0 and lista.count(num)>1]
paresDublicados = [num for num in lista if num%2==1 and num<0]
print(imparesNegativos)
print(paresDublicados)