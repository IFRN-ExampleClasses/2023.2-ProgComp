from variaveis import *

# Gerando uma lista onde cada elemento é uma "sub-lista"
# no formato [sigla, capital, populacao]
lstNordeste = list()
for pos in range(len(siglas)):
    lstNordeste.append([siglas[pos], capitais[pos], populacao[pos]])
print(f'\n{lstNordeste}\n')

# Ordenar a lista nordeste pelo nome da capital (A-Z)
lstNordeste.sort(key=lambda n:n[1])
print(f'\n{lstNordeste}\n')
