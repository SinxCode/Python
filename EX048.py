s=0
for c in range(1,500+1):
    if c % 2 == 1 and c % 3 == 0:
        print(c)
        s = s+c
print('O somatório dos números ímpares e múltiplos de 3 é: {}'.format(s))
       