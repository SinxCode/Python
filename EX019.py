import random
a = str(input('Digite o nome do primeiro aluno: '))
b = str(input('Digite o nome do segundo aluno: '))
c = str(input('Digite o nome do terceiro aluno: '))
d = str(input('Digite o nome do quarto aluno: '))
lista = [a,b,c,d]
sorteio = random.choice(lista)
print('O aluno sorteado foi: {}'.format(sorteio))


