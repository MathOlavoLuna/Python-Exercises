from string import ascii_uppercase

a = list(ascii_uppercase)
m = input('Digite a mensagem: ')
m = m.upper()
mc = ''

for l in m:
    i = ord(l)-65
    if l in a:
        mc += a[(i-4) % 26]
    else:
        i
print(f"Mensagem criptografada: {mc}")
