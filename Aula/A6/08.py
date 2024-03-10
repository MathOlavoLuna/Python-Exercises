notas = []
cont = 0
soma = 0

while True:
    enis = float(input('Digite a(s) nota(s): '))
    if enis <= 0:
        break
    else:
        notas.append(enis)
        cont += 1
for n in notas:
    soma += n
print(soma)
media = soma / cont
if media == ZeroDivisionError:
    print('No one value has typed for the math, Ending program...')

print(f'A média do aluno é {media}')
