f = input('Digite uma frase: ').strip().upper()
l = f.split()
j = ''.join(l)
#inverso = ''
inverso = j[::-1]
'''print('Você digitou: {}'.format(l))
for letra in range(len(j)-1, -1, -1):
    inverso = inverso + j[letra]'''
print('O inverso de {} é {}. '.format(j,inverso))    
if inverso == j:
    print('Temos um palíndromo')
else:
    print('Não é um palíndromo')