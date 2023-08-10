cidade = str(input('Digite o nome de sua cidade: '))
lista = cidade.upper().split()
inicio = lista[1]
print('Sua cidade começa com "SANTO"? {}'.format('SANTO' in lista))