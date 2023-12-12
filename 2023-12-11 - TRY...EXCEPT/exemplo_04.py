import sys

lista = [x for x in range(100) if x % 3 == 0]

pos = 50

try:
    print(lista[pos])
except IndexError:
    print('A posição informada não existe na lista')
except:
    print(f'ERRO.... {sys.exc_info()[0]}')
