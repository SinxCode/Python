d = int(input('Quantos dias ficou em posse do veículo? '))
km = float(input('Quantos KM o veículo percorreu? '))
pago = d * 60
pagokm = km * 0.15
print('O total da locação a pagar é de {}'.format(pago+pagokm))