import pandas as pd

x = {"Fons": [35, 34, 26, 32, 37, 28, 27, 33, 36, 32]}
p = pd.DataFrame(x)
media = p['Fons'].mean()
moda = p['Fons'].mode()
mediana = p['Fons'].median()
dp = p['Fons'].std()
print(f'Média: {media}')
print(f'Moda: {moda}')
print(f'Mediana: {mediana}')

print(f'Devio-Padrão: {dp}')