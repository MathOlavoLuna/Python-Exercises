def LeianInt(x=0, a=0):
    a = int(input('Digite um número inteiro: '))
    x = a
    return x


def LeiaFloat(x=0.0,b=0):
    b = float(input('Digite um número Real: '))
    x = b
    return x


while True:
    try:
        a = LeianInt()
    except ValueError:
        print('ERRO DIGITE UM NÙMERO INTEIRO')
        continue

    except KeyboardInterrupt:
        a = 0
        print('O usuário preferiu parar o programa')
        break
    else:
        break

while True:
    try:
        b = LeiaFloat()
    except ValueError:
        print('ERRO DIGITE UM NÙMERO real')
        continue
    except KeyboardInterrupt:
        b = 0
        print('O usuário preferiu parar o programa')
        break
    else:
        break

print(f'O número inteiro é {a} e o número real é {b}')
