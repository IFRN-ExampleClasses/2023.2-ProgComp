# Declarando o dicionário
dictNE = {'AL': {'capital': 'Maceió', 'populacao': 1018948}, 
          'BA': {'capital': 'Salvador', 'populacao': 2872347}, 
          'CE': {'capital': 'Fortaleza', 'populacao': 2669342}, 
          'MA': {'capital': 'São Luís', 'populacao': 1101884}, 
          'PB': {'capital': 'João Pessoa', 'populacao': 809015}, 
          'PE': {'capital': 'Recife', 'populacao': 1695727}, 
          'PI': {'capital': 'Teresina', 'populacao': 868075}, 
          'RN': {'capital': 'Natal', 'populacao': 890480}, 
          'SE': {'capital': 'Aracaju', 'populacao': 657013}
          }

# Abrindo o arquivo no mode de escrita (w) e aceitando
# caracteres acentuados (utf-8)
arqCapitais = open('nordeste_4.txt', 'w', encoding='utf-8')

# Escrevendo os itens do dicionário no arquivo
for k, v in dictNE.items():
    arqCapitais.write(f'{v["capital"]}/{k}:{v["populacao"]}\n')

# Escrevendo os dados do estado com a maior população
strUFMaiorPop = max(dictNE, key=lambda estado: dictNE[estado]['populacao'])
arqCapitais.write(f'\nCapital Mais Populosa: {dictNE[strUFMaiorPop]["capital"]}/{strUFMaiorPop}\n')
arqCapitais.write(f'População: {dictNE[strUFMaiorPop]["populacao"]}')

# Fechando o arquivo
arqCapitais.close()