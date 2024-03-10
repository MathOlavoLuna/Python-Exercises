#TRIÂNGULOS CARALHO
print('NÂO USE 0, NEM VALORES QUE A SOMA SEJA MENOR QUE 1 DOS VALORES')
a = float(input('Digite 1° valor: '))
b = float(input('Digite 2° valor: '))
c = float(input('Digite 3° valor: '))
if a == 0 or b == 0 or c == 0:
    print('Esse angulos não formam um trinânuglo por conta do 0')
else:
    if (a + b) > c and (b + c) > a and (c + a) > b:
        if a == b and a == c and b == c:
            print('Esses valores formam um triangulo Equilátero')
        elif a != b and b != c and c != a:
            print('Esse valores formam um triângulo Escaleno')
        else:
            print('Esses valores formam um triângulo Isósceles')
    else:
        print('coco')