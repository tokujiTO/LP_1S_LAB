condicao = False
while not condicao:
    codigo = input("Digite o código de conversão: ").upper()
    if codigo in "FC":
        condicao = True
    else:
        print("Código inválido! Por favor, digite C ou F.")
if codigo == "F":
    temp = int(input("Digite a temperatura em Farenheit: "))
    convert = (temp - 32) * 5 / 9
    print(f"Conversão - Temperatura em graus Celsius = {convert:.2f}")
else:
    temp = int(input("Digite a temperatura em Celsius: "))
    convert = temp * 9 / 5 + 32
    print(f"Conversão - Temperatura em graus Farenheit = {convert:.2f}")