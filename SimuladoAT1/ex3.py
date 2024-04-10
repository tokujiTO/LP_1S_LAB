estacao = int(input("""Digite sua estação preferida: 
                    [1] VERÃO 
                    [2] OUTONO
                    [3] INVERNO
                    [4] PRIMAVERA
                    """))
match estacao:
    case 1:
        print("Va para a praia!")
    case 2:
        print("Faça uma trilha!")
    case 3:
        print("Assista uma série!")
    case 4:
        print("Passeie no parque!")