siglas = ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE']

capitais = ['Maceió', 'Salvador', 'Fortaleza', 'São Luís', 'João Pessoa', 
            'Recife', 'Teresina', 'Natal', 'Aracaju']

populacao = [1018948, 2872347, 2669342, 1101884, 809015, 1695727,
             868075, 890480, 657013]

# Montando o Dicionário
dictNE = dict()
p = 0
for s in siglas:
    dictNE[s] = {'capital': capitais[p], 'populacao': populacao[p]}
    p += 1

print(dictNE)