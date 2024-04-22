def saida(galoes, horas, custoRelativo, taxa, custoTotal):
    print('-=-'*20)
    print(f"Foram necessários {galoes} galões para realizar o serviço")
    print(f"A quantidade de horas prevista são da ordem de {horas} horas")
    print(f"O custo relativo da tinta é de ${custoRelativo:.2f}")
    print(f"A taxa da mão de obra associada é de ${taxa:.2f}")
    print(f"O custo TOTAL de obra é de ${custoTotal:.2f}")
    return ()