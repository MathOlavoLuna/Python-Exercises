def soma(*num):
    soma = 0
    print(f'Tupla: {num}')
    for i in num:
        soma += i
    return soma


print(f'Resultado: {soma(1,2)}\n')
print(f'Resultado: {soma(1, 2, 3, 4, 5, 6, 7, 8, 9)}\n')
