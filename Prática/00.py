#ex01
v1 = str(input('Digite qualquer frase ou palavra: '))
tam = len(v1)
v2 = v1[:int(tam / 2)]
print(f'Os ultimos caracteres da sua string são ' + v2[-2:])
print(v2)
