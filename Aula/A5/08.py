def valida_str(texto, min, max):
    x = len(texto)
    while x < min or x > max:
        return True
    else:
        return False



texto = input('Digite uma string entre 3-15 caracteres: ')
while valida_str(texto, 3, 15):
    texto = input('Digite uma string entre 3-15 caracteres: ')
print(f'Você digitou a string: {texto}')