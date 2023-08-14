print('-='*30)
print('Verificação Alistamento Militar!')
idade = int(input('Digite sua idade: '))
if idade == 18:
    print('Está na hora de se alistar, guerreiro!')
elif idade > 18:
    print('Alistamento atrasado em {} meses! Alguém vai capinar mato!'.format((idade * 12) / idade))
else:
    print('Seu alistamento deverá ser feito em {} meses!'.format((idade * 12)/idade))
print('-='*30)
