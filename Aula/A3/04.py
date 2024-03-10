cima = True
baixo = True

while cima and baixo == True:
    print("Decida-se")
    print('Opção 1 CIMA')
    print('Opção 2 BAIXO')
    op = int(input(': '))
    if op == 1:
        baixo = False
        print('Você foi para cima')
    elif op == 2:
        cima = False
        print('Você foi para baixo')