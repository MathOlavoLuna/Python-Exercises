notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

print(max(notas))
notas.sort()
soma = 0
cont = 0
for nota in notas:
    soma += nota
    cont += 1
media = soma / cont
print(media)
