v_Desconto = 0
print('Bem vindo a loja do Matheus Olavo Marques Luna')  # Indentificador
valorProduto = float(input('Digite o valor unitário do seu produto: '))
quantidade = int(input('Quantas unidades dele você deseja?: '))

total = valorProduto * quantidade  # Pega o valor do produta e faz vezes a quantidade, assim gerando o total a ser pago.

print(f'O valor total do seu produto é: R${total:.2f}')

if quantidade <= 9:
    v_Desconto = 0

elif quantidade <= 99:
    v_Desconto = total * (5 / 100)
    numerozin = 5  # Só para ficar parecido com o exemplo.

elif quantidade <= 999:
    v_Desconto = total * (10 / 100)
    numerozin = 10

else:
    v_Desconto = total * (15 / 100)
    numerozin = 15

valorF = total - v_Desconto  # Variável que faz o valor total menos o desconto aplicado.

if v_Desconto > 9:  # Botei isso para caso o desconto não seja aplicado, a frase não será mostrada também.
    print(f'Por conta do seu desconto o valor fica: R${valorF:.2f} (Desconto de {numerozin}%)')
