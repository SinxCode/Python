import random
import emoji
#:1st_place_medal:
#:loudly_crying_face:
#:smiling_face_with_horns:
#:smiling_face_with_sunglasses:
#:chicken:

print( emoji.emojize('Olá! Você Gosta de jogos? Pois muito bem, o que acha de tentar me vencer? :smiling_face_with_horns:'))
escolha = str(input('Deseja tentar vencer a máquina? (S) ou (N)?'))
if escolha.upper()=='S':
    print('Que comece o jogo!')
    n = random.randint(1, 5)
    resultado = int(input('Eu acabei de pensar em número inteiro de 1 a 5, adivinhe qual é: '))
    if resultado == n:
        print(emoji.emojize('Parabéns! Você me venceu! :1st_place_medal:'))
    else:
        print(emoji.emojize('Hahahaha! :smiling_face_with_sunglasses: Você perdeu! Chore para mamãe :loudly_crying_face: '))
else: print(emoji.emojize('Foi o que pensei... covarde! :chicken:'))


