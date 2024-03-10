for n in range(2, 99, 1):
    flag = 0
    for i in range(2, n, 1):
        if n % i == 0:
            flag = 1
    if not flag:
        print(n)