def div():
    try:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite um número: '))
        res = num1 / num2
    except ZeroDivisionError:
        print('Erro de divisão por zero')
    except:
        print('Algo de errado aconteceu')
    else:
        return res
    finally:
        print('SEMPRE APARECERÁ, SEXO')


print(div())
