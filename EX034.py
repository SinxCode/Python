s = float(input('Digite o valor do seu salário: '))
if s > 1250:
    a=s * 0.10
else:
    a = s * 0.15
print('O seu aumento será de: {}\nO valor corrigido é: {} '.format(a, s + a))    