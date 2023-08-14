print('\033[0;30;41mOlá Mundo!\033[m') #Fundo vermelho, letra branca
print('\033[4;33;44mOlá Mundo!\033[m') #Fundo Azul, letra branca
print('\033[1;35;43mOlá Mundo!\033[m')#Fundo amarelo, letra roxa
print('\033[30;42mOlá Mundo!\033[m')#Fundo verde, letra branca
print('\033[mOlá Mundo!')#Fundo preto, letra cinza
#print('\033[7;30mOlá Mundo![m')

nome = 'Sinx'
cores = {'Limpa':'\033[m',
         'Azul':'\033[34m',
         'Amarelo':'\033[33m',
         'PretoeBranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhe conhecer {}{}{}!'.format(cores['Azul'],nome,cores['Limpa']))