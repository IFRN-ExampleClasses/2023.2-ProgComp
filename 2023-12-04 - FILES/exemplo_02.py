# Declarando as listas
capitais = ['Maceió', 'Salvador', 'Fortaleza', 'São Luís', 'João Pessoa', 
            'Recife', 'Teresina', 'Natal', 'Aracaju']

siglas = ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE']

populacao = [1018948, 2872347, 2669342, 1101884, 809015, 1695727,
             868075, 890480, 657013]


# Abrindo o arquivo no mode de escrita (w) e aceitando
# caracteres acentuados (utf-8)
arqCapitais = open('nordeste_2.txt', 'w', encoding='utf-8')

# Escrevendo os itens das listas no arquivo
for c, s, p in zip(capitais, siglas, populacao):
    arqCapitais.write(f'{c}/{s}:{p}\n')

# Fechando o arquivo
arqCapitais.close()