def relol(fim, inicio=0, c=1):
    for i in range(inicio, fim + 1, c):
        print(i, end=' ')
    print('\n')


relol(10)
relol(15, 2, 2)
