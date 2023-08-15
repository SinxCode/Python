n = int(input('Digite um número inteiro para o cálculo de sua tabuada: '))
m = 0
print('=-'*20)
for c in range (1, 10+1):
    m = n * c
    print('{} * {} = {}'.format(c,n,m))
print('=-'*20)    
print('Fim')    