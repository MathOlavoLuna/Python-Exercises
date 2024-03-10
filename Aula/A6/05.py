mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print(mochila[0][0:3])
for item in mochila:
    for l in item:
        print(f"{l}", end='')
    print()