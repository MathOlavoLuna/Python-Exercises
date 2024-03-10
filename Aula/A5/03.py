def v3(a=0, b=0, c=0):
    if a and b and c:
        if a > b and a > c:
            if b > c:
                print(f'Ordem decrescente: {a}, {b}, {c}')
            else:
                print(f'Ordem decrescente: {a}, {c}, {b}')
    if b > a and b > c:
        if a > c:
            print(f'Ordem decrescentee: {b}, {a}, {c}')
        else:
            print(f'Ordem decrescente: {b}, {c}, {a}')
    if c > a and c > b:
        if a > b:
            print(f'Ordem decrescente: {c}, {a}, {b}')
        else:
            print(f'Ordem decrescente: {c}, {b}, {a}')



v3(5,3,2)
