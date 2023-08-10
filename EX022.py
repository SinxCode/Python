nome = str(input('Digite seu nome: '))
maisculo = nome.upper()
minusculo = nome.lower()
letras = len(nome.replace(" ", ""))#conta a quantidade de letras no nome sem os espaços
lista = (nome.split())
contagem = len(lista[1])#conta quantidade de letras do primeiro nome
print(maisculo)
print(minusculo)
print(letras)
print(contagem)