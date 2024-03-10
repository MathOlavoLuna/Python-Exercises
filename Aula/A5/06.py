def valida_str(texto, min, max):
    if len(texto) < min or len(texto) > max:
      return False
    else:
        return True



texto = (input(': '))
print(valida_str(texto, 3, 15))
