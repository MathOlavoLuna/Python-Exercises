cadastro = {'nome': [], 'nascimento': [], 'sexo': []}
cu = []
mulheres = []
homens = []
hv = []
c = 0
anoAtual = 2023
soma = 0
while True:
    c += 1
    nome = str(input('Digite seu nome: '))
    ano = int(input('Em que ano você nasceu?: '))
    idadereal1 = anoAtual - ano
    sexo = str(input('Qual seu sexo?[M/F]: ').upper())

    if sexo == 'F' and idadereal1 < 30:
        mulheres.append(nome)

    elif sexo == 'M' and idadereal1 > 30:
        homens.append(nome)
        homens.append(idadereal1)

    cadastro['nome'].append(nome)
    cadastro['nascimento'].append(idadereal1)
    cadastro['sexo'].append(sexo)

    continua = str(input('Deseja Cadastrar mais alguem?[S/N]: ').lower())
    while continua not in 'sn':
        continua = str(input('Deseja Cadastrar mais alguem?[S/N]: ').lower())
    if continua == 'n':
        break

for numero in cadastro['nascimento']:
    soma += numero
media = soma / c

print(f'Total de cadastros efetuados: {c}')
print()
print(f'A média das idades das pessoas: {media:.2f}')
print()
print('Mulheres com menos de 30 anos:')
for m in mulheres:
    print(f' - {m}')
print()
print('Homens com idade maior que a média: ')
for h in homens:
    print(f'{h} ', end='')
