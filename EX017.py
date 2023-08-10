from math import sqrt
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
h = sqrt(co * co + ca * ca)
print('A hipotenusa referente os catetos:\nCO = {}\nCA = {} é: {:.2f}'.format(co,ca,h))