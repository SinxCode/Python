from datetime import datetime
ano = datetime.now().year
print(ano)
maior=0
menor =0
for c in range(0,7):
    a = int(input('Digite o ano de seu nascimento: '))
    if (ano - a) >= 18:
        maior = maior+1
    else:
        menor = menor +1
print('{} pessoas são maiores de idade e {} são menores de idade.'.format(maior,menor))


