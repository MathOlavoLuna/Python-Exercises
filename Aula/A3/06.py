print('1 - Residencial')
print('2 - Comercial')
print('3 - Industrial')
ti = int(input('Qual seu tipo de instalação?: '))
preco = float(0)
kwh = int(input('Quantos kWh você consome?: '))
if ti == 1:
    if kwh > 500:
        preco = kwh * 0.65
    else:
        preco = kwh * 0.40
elif ti == 2:
    if kwh > 1000:
        preco = kwh * 0.60
    else:
        preco = kwh * 0.55
else:
    if kwh > 5000:
        preco = kwh * 0.60
    else:
        preco = kwh * 0.55
print(f'Você tera de pagar {preco:.2f}R$')
