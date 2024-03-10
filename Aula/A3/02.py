print(('-='*8) + 'PC DO VINICIUS' + ('-='*8))
nome = str(input('Digite seu nome?: '))
idade = int(input('Qual sua idade?: '))
if nome == 'Vinicius':
    print('Saudade de você, Vinicius')
elif idade < 18:
    print('Você não é o vinicius e é menor de idade')
elif idade > 100:
    print('Certamente o Vinicius não é imortal, diferente de você')
