import math
ang = int(input('Digite o ângulo: '))
rad = math.radians(ang)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print('O valor do Seno é: {:.2f}\nO valor do Cosseno é: {:.2f}\nO Valor da Tangente é {:.2f}'.format(sen,cos,tan))