import pygame
from random import randint
from time import sleep
cores = {'Limpa':'\033[m',
         'Azul':'\033[34m',
         'Amarelo':'\033[33m',
         'Branco':'\033[30m',
         'Vermelho':'\033[31m',
          'Verde':'\033[32m'}
pygame.init()
pygame.mixer.music.load('Alex Kidd in the Enchanted Castle Mega Drive Title Music.mp3')
pygame.mixer.music.play()

print('-='* 30)
jkp = 'JAN KEN PO'
start = 'Aperte qualquer tecla para jogar!'
print('=-'*30)
print('{} {} {}'.format(cores['Amarelo'], jkp.center(55), cores['Limpa']))
print('=-'*30)
print(input(start.center(55)))
pygame.mixer.music.load('Alex kidd   Janken Match Opening_41ntBUSh6tM.mp3')
pygame.mixer.music.play()
print('=-'*30)
jogador = int(input('''Selecione uma das opções:
                    [1] Pedra,
                    [2] Tesoura,
                    [3] Papel 
                   Sua escolha: '''))
maquina = randint(1,3)
print('=-'*30)
pygame.mixer.music.load('Alex Kidd in the Enchanted Castle - Janken_tx-zijzZLIo.mp3')
pygame.mixer.music.play()
sleep(11)
pygame.mixer.music.load('14. _Jan-Ken-Pon__ - Alex Kidd Mega Drive Soundtrack (Sega)_7iQqkre2a4k.mp3')
pygame.mixer.music.play()
print('{}JAN{}'.format(cores['Azul'],cores['Limpa']))
sleep(0.4)
print('{}KEN{}'.format(cores['Azul'],cores['Limpa']))
sleep(0.6)
print('{}PO{}'.format(cores['Azul'], cores['Limpa']))
print('=-'*30)
sleep(1)
print('Escolha da máquina: {}'.format(maquina))
if jogador == 1 and maquina == 2: #Jogador escolheu Pedra (1)
    pygame.mixer.music.load('15. Win__ - Alex Kidd Mega Drive Soundtrack (Sega)_YzGL8-DlGr4.mp3')
    pygame.mixer.music.play()
    print('{}Jogador venceu!{}'.format(cores['Verde'],cores['Limpa']))
elif jogador == 1 and maquina == 3:
    pygame.mixer.music.load('16. Lose__ - Alex Kidd Mega Drive Soundtrack (Sega).mp3')
    pygame.mixer.music.play()
    print('{}Jogador Perdeu!{}'.format(cores['Vermelho'],cores['Limpa']))
elif jogador ==1 and maquina ==1:
    pygame.mixer.music.load('16. Lose__ - Alex Kidd Mega Drive Soundtrack (Sega).mp3')
    pygame.mixer.music.play()
    print('Empate!')
if jogador == 2 and maquina == 3: #Jogador escolheu tesoura (2)
    pygame.mixer.music.load('15. Win__ - Alex Kidd Mega Drive Soundtrack (Sega)_YzGL8-DlGr4.mp3')
    pygame.mixer.music.play()
    print('{}Jogador venceu!{}'.format(cores['Verde'],cores['Limpa']))
elif jogador == 2 and maquina == 1:
    pygame.mixer.music.load('16. Lose__ - Alex Kidd Mega Drive Soundtrack (Sega).mp3')
    pygame.mixer.music.play()
    print('{}Jogador Perdeu!{}'.format(cores['Vermelho'],cores['Limpa']))
elif jogador ==2 and maquina ==2:
    pygame.mixer.music.load('16. Lose__ - Alex Kidd Mega Drive Soundtrack (Sega).mp3')
    pygame.mixer.music.play()
    print('Empate!')
if jogador == 3 and maquina == 1: #Jogador escolheu papel (3)
    pygame.mixer.music.load('15. Win__ - Alex Kidd Mega Drive Soundtrack (Sega)_YzGL8-DlGr4.mp3')
    pygame.mixer.music.play()
    print('{}Jogador venceu!{}'.format(cores['Verde'],cores['Limpa']))
elif jogador == 3 and maquina == 2:
    pygame.mixer.music.load('16. Lose__ - Alex Kidd Mega Drive Soundtrack (Sega).mp3')
    pygame.mixer.music.play()
    print('{}Jogador Perdeu!{}'.format(cores['Vermelho'],cores['Limpa']))
elif jogador ==3 and maquina ==3:
    pygame.mixer.music.load('16. Lose__ - Alex Kidd Mega Drive Soundtrack (Sega).mp3')
    pygame.mixer.music.play()
    print('Empate!')
    print('=-'*30)
print(input('Aperte algo para sair'))



