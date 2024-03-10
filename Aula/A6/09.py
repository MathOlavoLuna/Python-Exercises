try:
    notas = []
    x = float(input('Digita uma nota: '))
    while x >= 0:
        notas.append(x)
        x = float(input('Digita uma nota: '))
    soma = 0
    for i in notas:
        soma += i
    media = soma / len(notas)
    print(notas)
    print(f'Média das notas digitas: {media}')
except ZeroDivisionError:
    print('Encerrado programa fdp')