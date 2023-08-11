from calendar import isleap
a = int(input('Digite um ano: '))
if isleap(a):
    print('O ano é bissexto!')
else:
    print('O ano não é bissexto!')