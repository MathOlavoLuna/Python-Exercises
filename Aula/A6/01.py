mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
print(mochila)
print(mochila[0])
print(mochila[2])
print(mochila[0:2])
print(mochila[2:])
print(mochila[-1])
print()
cont = 1
tam = len(mochila)
for i in range(0, tam, 1):
    print(mochila[i])
print()

for item in mochila: 
    print(f'{cont}° : {item}')
    cont += 1

upgrade = ('Queijo', 'Canivete')
mochila_grande = upgrade + mochila
print(mochila_grande)
print()
