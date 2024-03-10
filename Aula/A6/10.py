games = []
game1 = {'nome': 'Super Mario', 'videogame': ' Super Nintendo', 'ano': 1990}

game2 = {'nome': 'Zelda Ocarina of Time', 'videogame': ' Nintendo 64', 'ano': 1998}

game3 = {'nome': 'Pokemon', 'videogame': ' Gameboy', 'ano': 1999}

games = [game1, game2, game3]
for i in games:
    for j, x in i.items():
        print(f'{j} = {x}')

