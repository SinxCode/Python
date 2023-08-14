n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
if media <5:
    print('Sua média é {}! Infelizmente, reprovado!'.format(media))
elif media >= 5 and media <= 6.9:
    print('Sua média é {}! Ficará de recuperação!'.format(media))
else:
    print('Parabéns! Sua média é: {}! Aprovado!'.format(media))