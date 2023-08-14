valor = float(input('Digite o valor do produto: '))
condicao = int(input('''Informe a condição: 
                 [1] Cheque/Dinheiro a vista,
                 [2] Cartão a vista,
                 [3] Até 2x cartão,
                 [4] Acima de 3x cartão\n''' ))
if condicao ==1:
    desconto = valor * 0.10
    print('O produto obteve um desconto de 10%!')
    print('Valor descontado: {:.2f} '.format(desconto))
    print('Valor a pagar: {:.2f}'.format(valor - desconto))
elif condicao ==2:
    desconto = valor * 0.05
    print('O produto obteve um desconto de 5%!')
    print('Valor descontado: {:.2f} '.format(desconto))
    print('Valor a pagar: {:.2f}'.format(valor - desconto))
elif condicao == 3:
    desconto = 0
    print('O produto não obteve desconto')
    print('Valor descontado: {:.2f} '.format(desconto))
    print('Valor a pagar: {:.2f}'.format(valor - desconto))
else:
    juros = valor * 0.20
    print('O produto obteve um acréscimo de 20% de juros!')
    print('Valor de juros: {:.2f} '.format(juros))
    print('Valor a pagar: {:.2f}'.format(valor + juros))