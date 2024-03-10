
#Contador---------
inicial = int(input('Valor inicial da contagem?: '))
final = int(input('Valor final da contagem?: '))
x = inicial
while (x <= final):
    if x % 3 == 0:
        print(x)
    x += 1
#Acumulador
soma = 0
cont = 1
while cont <= 5:
    x = float(input(f'Digite a {cont}ª nota: '))
    soma += x
    cont += 1
media = soma / 5
print(f'Média final: {media}')
