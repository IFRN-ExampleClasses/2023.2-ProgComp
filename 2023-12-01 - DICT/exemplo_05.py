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

# Ordenando o dicionário pela população decrescente
fun_ordena = lambda uf: uf[1]['populacao']
dictNE_ord = sorted(dictNE.items(), key=fun_ordena, reverse=True)
dictNE_ord = dict(dictNE_ord)

# Imprimindo os itens do dicionário
for k, v in dictNE_ord.items():
    print(f'{k}/{v["capital"]} ..... {v["populacao"]}')