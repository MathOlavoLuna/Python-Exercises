d = int(input('Pôr quantos dias você alugou o carro?: '))
km = float(input(f'Quantos Km você percorreu dutante esses {d} dias?: '))
calc = (d * 60) + (km * 0.15)
print(f'O preço total a pagar pelo carro alugado será {calc:.2f}R$')