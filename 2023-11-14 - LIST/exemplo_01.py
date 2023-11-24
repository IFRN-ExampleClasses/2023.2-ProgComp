media = 0

contador = 0
lista = list()

while contador < 10:
    valor  = int(input('Digite um valor: '))
    lista.append(valor)
    media    += valor
    contador += 1

media = media/10
lista.sort()

print(f'Média dos valores: {media}')
print(f'Maior Valor......: {lista[0]}')
print(f'Maior Valor......: {lista[9]}')