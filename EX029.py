v = float(input('Digite a velocidade do veículo em km/h: '))
m = 7
if v > 80:
    print('A velocidade ultrapassou o limite de 80km/h! O carro será multado em: {:.2f}'.format(v * m))
else: print('Velocidade normal.')