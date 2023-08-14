print('-='*30)
print('Classificação de Atletas!')

idade = int(input('Digite a idade do atleta: '))
if idade <= 9:
    print('Categoria Mirim!')
elif idade <=14:
    print('Categoria infantil!')
elif idade <=19:
    print('Categoria Junior!')
elif idade <=20:
    print('Categoria Senior!')
else:
    print('Categoria Master!')
print('-='*30)