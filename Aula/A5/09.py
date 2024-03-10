def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while x < min or x > max:
        x = int(input(pergunta))
    return x


x = valida_int('Digite seu número inteiro: ', 3, 25)
print(x)
