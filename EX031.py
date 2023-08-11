n = float(input('Digite a distancia da viagem a ser percorrida em KM: '))
if n <= 200:
    print('O valor da passagem será de: {:.2f}'.format(n * 0.5))
else:
    print('O valor da passagem será de: {:.2f}'.format(n * 0.45))
