n = int(input('Digite um número inteiro: '))
print('''Escolhas uma das bases para conversão:
      [1] converter para BINÁRIO
      [2] converter para OCTAL
      [3] converter para HEXADECIMAL''')
opcao = int (input('Sua opção: '))
if  opcao ==1:
    print('{} convertido para BINÁRIO é: {}'.format(n,bin(n)[2:]))
elif opcao ==2:
     print('{} convertido para OCTAL é: {}'.format(n,oct(n)[2:]))
elif opcao==3:
     print('{} convertido para HEXADECIMAL é: {}'.format(n,hex(n)[2:]))
else:
     print('Opção inválida, tente novamente.')

