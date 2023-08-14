cores = {'Limpa':'\033[m',
         'Azul':'\033[34m',
         'Amarelo':'\033[33m',
         'Branco':'\033[30m',
         'Vermelho':'\033[31m',
          'Verde':'\033[32m'}
print('-='* 30)
print('{}Veja se é possível realizar o seu financiamento!{}'.format(cores['Amarelo'],cores['Limpa']))
casa = float(input('Informe o valor do imóvel: '))
salario = float(input('Digite o valor de seu salário: '))
ano = int(input('Informe em quantos anos gostaria de quitar o imóvel: '))
parcelas = casa / (ano*12)
print('O Valor das parecelas em {} anos é de {:.2f} mensais!'.format(ano, parcelas))
porcentagem = salario * 0.3
if parcelas > porcentagem:
    print('{}Infelizmente não será possível realizar o financiamento do imóvel!{}'.format(cores['Vermelho'],cores['Limpa']))
else:
    print('{}Parabéns, você pode financiar esse imóvel!{}'.format(cores['Verde'],cores['Limpa']))
