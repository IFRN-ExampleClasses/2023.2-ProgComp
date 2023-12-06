# Declarando a lista
lstCapitais = [
                ['AL', 'Maceió', 1018948], 
                ['BA', 'Salvador', 2872347], 
                ['CE', 'Fortaleza', 2669342], 
                ['MA', 'São Luís', 1101884], 
                ['PB', 'João Pessoa', 809015], 
                ['PE', 'Recife', 1695727], 
                ['PI', 'Teresina', 868075], 
                ['RN', 'Natal', 890480], 
                ['SE', 'Aracaju', 657013]
            ]

# Abrindo o arquivo no mode de escrita (w) e aceitando
# caracteres acentuados (utf-8)
arqCapitais = open('nordeste_2b.txt', 'w', encoding='utf-8')

# Escrevendo os itens da lista no arquivo
for cidade in lstCapitais:
    arqCapitais.write(f'{cidade[1]}/{cidade[0]}:{cidade[2]}\n')

# Escrevendo os dados do estado com a maior população
lstDadosMaiorPop = max(lstCapitais, key=lambda estado: estado[2])
arqCapitais.write(f'\nCapital Mais Populosa: {lstDadosMaiorPop[1]}/{lstDadosMaiorPop[0]}\n')
arqCapitais.write(f'População: {lstDadosMaiorPop[2]}')

# Fechando o arquivo
arqCapitais.close()