while True:
    nome = str(input('Qual seu nome?: '))
    if nome != 'Luna':
        continue
    senha = input('Qual a sua senha?: ')
    if senha == 'MuRaD61-':
        break
print('Acesso concedido.')