
#Truety Falsey

nome = ''
while not nome:
    nome = str(input('Digite seu nome: '))
valor = int(input('Digite um número qualquer: '))
if valor:
    print(f'Seu nome é {nome} e')
    print('Você digitou um número diferente de zero')
else:
    print(f'Seu nome é {nome} e')
    print('você digitou zero.')
