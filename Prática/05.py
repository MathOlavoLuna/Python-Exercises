x = int(input('Digite um valor: '))
c1 = 1
c2 = 5
c3 = 10
c4 = 20
c5 = 50
c6 = 100
if x >= c6:
    ced100 = x // 100
    x -= ced100 * 100
    print(f'Cédulas de 100R$ Sacadas: {ced100}')

if x >= c5:
    ced50 = x // 50
    x -= ced50 * 50
    print(f'Cédulas de 50R$ sacadas: {ced50}')

if x >= c4:
    ced20 = x // 20
    x -= ced20 * 20
    print(f'Cédulas de 20R$ sacadas: {ced20}')

if x >= c3:
    ced10 = x // 10
    x -= ced10 * 10
    print(f'Cédulas de 10R$ sacadas: {ced10}')

if x >= c2:
    ced5 = x // 5
    x -= ced5 * 5
    print(f'Cédulas de 5R$ sacadas: {ced5}')

if x:
    ced1 = x
    print(f'Cédulas de 1R$: {ced1}')