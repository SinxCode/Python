n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
r = n1 % n2
print('A soma é {},\nO produto é {},\nA divisão é, {:.3f}\n' .format(s,m,d), end='') #end serve para continuar com o segundo print
print('A divisão inteira é {}, a exponenciação é {} e o resto da divisão é {}'.format(di, e, r))

