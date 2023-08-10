numero = int(input('Digite um número inteiro de 0 a 9999: '))
conversao = str(numero)
unidade = conversao[3]
dezena = conversao[2]
centena = conversao[1]
milhar = conversao[0]
print('O número digitado foi: {}'.format(numero))
print('Unidade:{} '.format(unidade))
print('Dezena:{} '.format(dezena))
print('Centena:{} '.format(centena))
print('Milhar:{} '.format(milhar))