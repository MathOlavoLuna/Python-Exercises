game = {}
games = []
for i in range(3):
    game['nome'] = input('Nome do jogo: ')
    game['videogame'] = input('Nome do console: ')
    game['ano'] = input('Ano de lançamento: ')
    games.append(game.copy())
print('-' * 20)
for e in games:
    for i, v in e.items():
        print(f'O campo {i} tem o valor {v}.')
