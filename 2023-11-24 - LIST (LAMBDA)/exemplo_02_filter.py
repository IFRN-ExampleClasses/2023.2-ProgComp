from variaveis import *

# Gerando uma lista onde cada elemento é uma "sub-lista"
# no formato [sigla, capital, populacao]
lstNordeste = list()
for pos in range(len(siglas)):
    lstNordeste.append([siglas[pos], capitais[pos], populacao[pos]])
print(f'\n{lstNordeste}\n')

# Filtrar as capitais com população >= 1000000
filtro = lambda n:n[2] >= 1000000
lstNE = list(filter(filtro, lstNordeste))
print(f'\n{lstNE}\n')
